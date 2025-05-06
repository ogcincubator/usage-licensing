import hashlib
import json
import re
import sys
from io import BytesIO
from pathlib import Path

import requests
from openpyxl import load_workbook
from rdflib import Graph, URIRef, Literal, RDF, DCTERMS

LICENSE_FIELDS = ('id', 'label', 'sameAs', 'url', 'description')
TERM_FIELDS = ('licenseId', 'type', 'actions', 'duties')
MAPPINGS_FIELDS = ('bpmn', 'id', 'title', 'url', 'usageLicense', 'wellKnownLicense')

USAGE_LICENSES_NS = 'https://w3id.org/usage-project/licenses/'
USAGE_ODRL_ACTIONS_NS = 'https://w3id.org/usage-project/odrl/actions/'

OUTPUT_DIR = Path('catalog')


def to_uri(s: str):
    if '#/metadata/' in s:
        root, dataset_id = s.split('#/metadata/', 1)
        root = root.replace('/igiljugb/', '/srv/')
        base, _ = root.split('/srv/', 1)
        s = f"{base}/srv/api/records/{dataset_id}"
    return URIRef(s)


def _main():
    print('Downloading spreadsheet...')
    xlsx_url = sys.argv[1]
    r = requests.get(xlsx_url)
    r.raise_for_status()

    print('Loading spreadsheet...')
    wb = load_workbook(BytesIO(r.content))

    print('Processing licenses...')
    licenses_ws = wb['USAGELicenses']
    licenses = {}
    for i, row in enumerate(licenses_ws.rows):
        if i == 0:
            continue
        if not row[0].value:
            break
        license = dict(zip(LICENSE_FIELDS, (c.value for c in row)))
        licenses[license['id']] = license
    print(len(licenses), 'licenses found')

    terms_ws = wb['USAGELicenseTerms']
    for i, row in enumerate(terms_ws.rows):
        if i == 0:
            continue
        if not row[0].value:
            break
        term = dict(zip(TERM_FIELDS, (c.value for c in row)))
        license = licenses.get(term['licenseId'])
        if not license:
            raise ValueError('Unknown license found in terms: {}'.format(term['licenseId']))
        license.setdefault('terms', []).append(term)

    output_licenses = []
    for license_entry in licenses.values():
        license = {
            'uid': 'usage-license:' + license_entry['id'],
            'type': 'Policy',
            'title': license_entry['label'],
        }
        if license_entry['url']:
            license['dct:source'] = license_entry['url']
        if license_entry['description']:
            license['dct:description'] = license_entry['description']
        if license_entry['sameAs']:
            license['owl:sameAs'] = { '@id': license_entry['sameAs'] }

        for term_entry in license_entry.get('terms', []):
            if not term_entry['actions']:
                continue
            term_type = term_entry['type'].lower()
            rules = license.setdefault(term_type, {})
            rules.setdefault('action', []).extend([a.strip()
                                                   for a in re.split(r', *', term_entry['actions'])
                                                   if a.strip()])
            if term_entry['duties']:
                duties = [d.strip() for d in re.split(r', *', term_entry['duties']) if d.strip()]
                if duties:
                    rules.setdefault('duties', []).extend(duties)

        output_licenses.append(license)

    licenses_jsonld = {
        '@context': [
            'https://ogcincubator.github.io/usage-licensing/build/annotated/usage-project/licensing/odrl/2/2/policy/context.jsonld',
            {
                'usage-license': USAGE_LICENSES_NS,
                'usage-action': USAGE_ODRL_ACTIONS_NS,
            }
        ],
        '@graph': output_licenses,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    licenses_jsonld_contents = json.dumps(licenses_jsonld, indent=2)
    with open(OUTPUT_DIR / 'usage-licenses.jsonld', 'w') as f:
        f.write(licenses_jsonld_contents)
    g = Graph().parse(data=licenses_jsonld_contents, format='json-ld')
    g.serialize(OUTPUT_DIR / 'usage-licenses.ttl', format='turtle')
    print(OUTPUT_DIR / 'usage-licenses.jsonld', 'and', OUTPUT_DIR / 'usage-licenses.ttl', 'written')

    print('Processing dataset mappings...')
    mappings_ws = wb['DatasetMappings']
    g = Graph()
    for i, row in enumerate(mappings_ws.rows):
        if i == 0:
            continue
        if not row[0].value:
            break
        mapping = dict(zip(MAPPINGS_FIELDS, (c.value for c in row)))

        if mapping['usageLicense'] or mapping['wellKnownLicense']:
            entity_uri = to_uri(mapping['url'])
            license_uri = URIRef(mapping['wellKnownLicense'] or f"{USAGE_LICENSES_NS}{mapping['usageLicense']}")
            g.add((entity_uri, DCTERMS.license, license_uri))
            if mapping['id'] != mapping['url']:
                g.add((entity_uri, DCTERMS.identifier, Literal(mapping['id'])))
            g.add((entity_uri, DCTERMS.title, Literal(mapping['title'])))
    g.serialize(OUTPUT_DIR / 'dataset-mappings.ttl', format='turtle')
    print(OUTPUT_DIR / 'dataset-mappings.ttl', 'written')

if __name__ == '__main__':
    _main()
