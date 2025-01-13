
# USAGE Provenance Schema (Schema)

`eu.usage-project.licensing.prov` *v0.1*

Schema for a provenance chain based on PROV, with additional USAGE terms

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Graz 30% of tree canopy coverage per district - simplified
![Part of the BPMN corresponding to the example](examples/uc-gr-30-bpmn-simplified-cropped.png)
#### json
```json
{
  "$schema": "https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/schema.json",
  "$comment": "Provenance representation of UC_GR_30-300-BPMN_simplified",

  "id": "https://usage.geocat.live/catalogue/srv/api/records/600de8b7-7683-4cb1-bc8d-ca1ac5c2145b",
  "type": "Entity",
  "title": "Graz 30% tree canopy rule (district level)",
  "wasGeneratedBy": {
    "featureType": "Activity",
    "description": "Calculate the % of coverage of high vegetation in each district and check if the percentage is >30%. Assign the characteristics to the district polygons.",
    "links": {
      "title": "30 percent criterion",
      "href": "https://usage.geocat.live/catalogue/srv/api/records/8309b176-983c-4460-8361-d55bd8829c9c"
    },
    "used": [
      {
        "id": "https://usage.geocat.live/catalogue/srv/api/records/4f18ca71-38e9-4d55-9064-bc5085a50608",
        "featureType": "Entity",
        "title": "Graz districts",
        "license": "cc-by4.0"
      },
      {
        "id": "https://usage.geocat.live/catalogue/srv/api/records/e6991462-e031-4deb-a362-c5b55139316a",
        "featureType": "Entity",
        "title": "Graz surface material classification map",
        "license": "cc-by-nc4.0"
      }
    ]
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://raw.githubusercontent.com/ogcincubator/usage-licensing/undefined/build/annotated/usage-project/licensing/prov/context.jsonld",
  "$schema": "https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/schema.json",
  "$comment": "Provenance representation of UC_GR_30-300-BPMN_simplified",
  "id": "https://usage.geocat.live/catalogue/srv/api/records/600de8b7-7683-4cb1-bc8d-ca1ac5c2145b",
  "type": "Entity",
  "title": "Graz 30% tree canopy rule (district level)",
  "wasGeneratedBy": {
    "featureType": "Activity",
    "description": "Calculate the % of coverage of high vegetation in each district and check if the percentage is >30%. Assign the characteristics to the district polygons.",
    "links": {
      "title": "30 percent criterion",
      "href": "https://usage.geocat.live/catalogue/srv/api/records/8309b176-983c-4460-8361-d55bd8829c9c"
    },
    "used": [
      {
        "id": "https://usage.geocat.live/catalogue/srv/api/records/4f18ca71-38e9-4d55-9064-bc5085a50608",
        "featureType": "Entity",
        "title": "Graz districts",
        "license": "cc-by4.0"
      },
      {
        "id": "https://usage.geocat.live/catalogue/srv/api/records/e6991462-e031-4deb-a362-c5b55139316a",
        "featureType": "Entity",
        "title": "Graz surface material classification map",
        "license": "cc-by-nc4.0"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdflicense: <http://purl.org/NET/rdflicense/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<https://usage.geocat.live/catalogue/srv/api/records/600de8b7-7683-4cb1-bc8d-ca1ac5c2145b> dct:title "Graz 30% tree canopy rule (district level)" ;
    prov:wasGeneratedBy [ a prov:Activity ;
            dct:description "Calculate the % of coverage of high vegetation in each district and check if the percentage is >30%. Assign the characteristics to the district polygons." ;
            rdfs:seeAlso [ rdfs:label "30 percent criterion" ;
                    oa:hasTarget <https://usage.geocat.live/catalogue/srv/api/records/8309b176-983c-4460-8361-d55bd8829c9c> ] ;
            prov:used <https://usage.geocat.live/catalogue/srv/api/records/4f18ca71-38e9-4d55-9064-bc5085a50608>,
                <https://usage.geocat.live/catalogue/srv/api/records/e6991462-e031-4deb-a362-c5b55139316a> ] .

<https://usage.geocat.live/catalogue/srv/api/records/4f18ca71-38e9-4d55-9064-bc5085a50608> a prov:Entity ;
    dct:license rdflicense:cc-by4.0 ;
    dct:title "Graz districts" .

<https://usage.geocat.live/catalogue/srv/api/records/e6991462-e031-4deb-a362-c5b55139316a> a prov:Entity ;
    dct:license rdflicense:cc-by-nc4.0 ;
    dct:title "Graz surface material classification map" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$comment: Reuse provenance chain schema
oneOf:
- $ref: https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/schema.yaml
- type: array
  items:
    $ref: https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/schema.yaml
x-jsonld-extra-terms:
  title: dct:title
  description: dct:description
  license:
    x-jsonld-id: dct:license
    x-jsonld-type: '@id'
    x-jsonld-context:
      '@base': http://purl.org/NET/rdflicense/
x-jsonld-prefixes:
  rdflicense: http://purl.org/NET/rdflicense/
  odrl: http://www.w3.org/ns/odrl/2/

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/ogcincubator/usage-licensing/undefined/build/annotated/usage-project/licensing/prov/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/ogcincubator/usage-licensing/undefined/build/annotated/usage-project/licensing/prov/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "id": "@id",
    "featureType": "@type",
    "entityType": "@type",
    "has_provenance": {
      "@id": "dct:provenance",
      "@type": "@id"
    },
    "wasGeneratedBy": {
      "@id": "prov:wasGeneratedBy",
      "@type": "@id"
    },
    "wasAttributedTo": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "prov:wasAttributedTo",
      "@type": "@id"
    },
    "wasDerivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@type": "@id"
    },
    "alternateOf": {
      "@id": "prov:alternateOf",
      "@type": "@id"
    },
    "hadPrimarySource": {
      "@id": "prov:hadPrimarySource",
      "@type": "@id"
    },
    "specializationOf": {
      "@id": "prov:specializationOf",
      "@type": "@id"
    },
    "wasInvalidatedBy": {
      "@id": "prov:wasInvalidatedBy",
      "@type": "@id"
    },
    "wasQuotedFrom": {
      "@id": "prov:wasQuotedFrom",
      "@type": "@id"
    },
    "wasRevisionOf": {
      "@id": "prov:wasRevisionOf",
      "@type": "@id"
    },
    "atLocation": {
      "@id": "prov:atLocation",
      "@type": "@id"
    },
    "links": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "qualifiedGeneration": {
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "xsd:dateTime"
        },
        "hadRole": {
          "@id": "prov:hadRole",
          "@type": "@id"
        },
        "influencer": {
          "@id": "prov:influencer",
          "@type": "@id"
        },
        "hadActivity": {
          "@id": "prov:hadActivity",
          "@type": "@id"
        },
        "activity": {
          "@id": "prov:activity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedGeneration",
      "@type": "@id"
    },
    "qualifiedInvalidation": {
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "xsd:dateTime"
        },
        "hadRole": {
          "@id": "prov:hadRole",
          "@type": "@id"
        },
        "influencer": {
          "@id": "prov:influencer",
          "@type": "@id"
        },
        "hadActivity": {
          "@id": "prov:hadActivity",
          "@type": "@id"
        },
        "activity": {
          "@id": "prov:activity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedInvalidation",
      "@type": "@id"
    },
    "qualifiedDerivation": {
      "@context": {
        "hadGeneration": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          },
          "@id": "prov:hadGeneration",
          "@type": "@id"
        },
        "hadActivity": {
          "@id": "prov:hadActivity",
          "@type": "@id"
        },
        "hadUsage": {
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "xsd:dateTime"
            }
          },
          "@id": "prov:hadUsage",
          "@type": "@id"
        },
        "entity": {
          "@id": "prov:entity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedDerivation",
      "@type": "@id"
    },
    "qualifiedAttribution": {
      "@context": {
        "agent": {
          "@id": "prov:agent",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedAttribution",
      "@type": "@id"
    },
    "wasInfluencedBy": {
      "@id": "prov:wasInfluencedBy",
      "@type": "@id"
    },
    "qualifiedInfluence": {
      "@context": {
        "influencer": {
          "@id": "prov:influencer",
          "@type": "@id"
        },
        "entity": {
          "@id": "prov:entity",
          "@type": "@id"
        },
        "activity": {
          "@id": "prov:activity",
          "@type": "@id"
        },
        "agent": {
          "@id": "prov:agent",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedInfluence",
      "@type": "@id"
    },
    "provType": "@type",
    "hadMember": {
      "@id": "prov:hadMember",
      "@type": "@id"
    },
    "activityType": "@type",
    "endedAtTime": {
      "@id": "prov:endedAtTime",
      "@type": "xsd:dateTime"
    },
    "wasAssociatedWith": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "wasInformedBy": {
      "@id": "prov:wasInformedBy",
      "@type": "@id"
    },
    "used": {
      "@id": "prov:used",
      "@type": "@id"
    },
    "wasStartedBy": {
      "@id": "prov:wasStartedBy",
      "@type": "@id"
    },
    "wasEndedBy": {
      "@id": "prov:wasEndedBy",
      "@type": "@id"
    },
    "invalidated": {
      "@id": "prov:invalidated",
      "@type": "@id"
    },
    "generated": {
      "@id": "prov:generated",
      "@type": "@id"
    },
    "qualifiedUsage": {
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "xsd:dateTime"
        },
        "entity": {
          "@id": "prov:entity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedUsage",
      "@type": "@id"
    },
    "qualifiedCommunication": {
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "xsd:dateTime"
        },
        "hadRole": {
          "@id": "prov:hadRole",
          "@type": "@id"
        },
        "influencer": {
          "@id": "prov:influencer",
          "@type": "@id"
        },
        "hadActivity": {
          "@id": "prov:hadActivity",
          "@type": "@id"
        },
        "activity": {
          "@id": "prov:activity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedCommunication",
      "@type": "@id"
    },
    "qualifiedStart": {
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "xsd:dateTime"
        },
        "entity": {
          "@id": "prov:entity",
          "@type": "@id"
        },
        "hadActivity": {
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedStart",
      "@type": "@id"
    },
    "qualifiedEnd": {
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "xsd:dateTime"
        },
        "entity": {
          "@id": "prov:entity",
          "@type": "@id"
        },
        "hadActivity": {
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedEnd",
      "@type": "@id"
    },
    "qualifiedAssociation": {
      "@context": {
        "agent": {
          "@id": "prov:agent",
          "@type": "@id"
        },
        "hadRole": {
          "@id": "prov:hadRole",
          "@type": "@id"
        },
        "hadPlan": {
          "@id": "prov:hadPlan",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedAssociation",
      "@type": "@id"
    },
    "agentType": "@type",
    "name": "rdfs:label",
    "actedOnBehalfOf": {
      "@id": "prov:actedOnBehalfOf",
      "@type": "@id"
    },
    "qualifiedDelegation": {
      "@context": {
        "agent": {
          "@id": "prov:agent",
          "@type": "@id"
        },
        "hadActivity": {
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedDelegation",
      "@type": "@id"
    },
    "Activity": "prov:Activity",
    "ActivityInfluence": "prov:ActivityInfluence",
    "Agent": "prov:Agent",
    "AgentInfluence": "prov:AgentInfluence",
    "Association": "prov:Association",
    "Attribution": "prov:Attribution",
    "Bundle": "prov:Bundle",
    "Collection": "prov:Collection",
    "Communication": "prov:Communication",
    "Delegation": "prov:Delegation",
    "Derivation": "prov:Derivation",
    "EmptyCollection": "prov:EmptyCollection",
    "End": "prov:End",
    "Entity": "prov:Entity",
    "EntityInfluence": "prov:EntityInfluence",
    "Generation": "prov:Generation",
    "Influence": "prov:Influence",
    "InstantaneousEvent": "prov:InstantaneousEvent",
    "Invalidation": "prov:Invalidation",
    "Location": "prov:Location",
    "Organization": "prov:Organization",
    "Person": "prov:Person",
    "Plan": "prov:Plan",
    "PrimarySource": "prov:PrimarySource",
    "Quotation": "prov:Quotation",
    "Revision": "prov:Revision",
    "Role": "prov:Role",
    "SoftwareAgent": "prov:SoftwareAgent",
    "Start": "prov:Start",
    "Usage": "prov:Usage",
    "ServiceDescription": "prov:ServiceDescription",
    "DirectQueryService": "prov:DirectQueryService",
    "Accept": "prov:Accept",
    "Contribute": "prov:Contribute",
    "Contributor": "prov:Contributor",
    "Copyright": "prov:Copyright",
    "Create": "prov:Create",
    "Creator": "prov:Creator",
    "Modify": "prov:Modify",
    "Publish": "prov:Publish",
    "Publisher": "prov:Publisher",
    "Replace": "prov:Replace",
    "RightsAssignment": "prov:RightsAssignment",
    "RightsHolder": "prov:RightsHolder",
    "Submit": "prov:Submit",
    "Dictionary": "prov:Dictionary",
    "EmptyDictionary": "prov:EmptyDictionary",
    "KeyEntityPair": "prov:KeyEntityPair",
    "Insertion": "prov:Insertion",
    "Removal": "prov:Removal",
    "generatedAtTime": {
      "@id": "prov:generatedAtTime",
      "@type": "xsd:dateTime"
    },
    "invalidatedAtTime": {
      "@id": "prov:invalidatedAtTime",
      "@type": "xsd:dateTime"
    },
    "startedAtTime": {
      "@id": "prov:startedAtTime",
      "@type": "xsd:dateTime"
    },
    "value": "prov:value",
    "provenanceUriTemplate": "prov:provenanceUriTemplate",
    "pairKey": {
      "@id": "prov:pairKey",
      "@type": "rdfs:Literal"
    },
    "removedKey": {
      "@id": "prov:removedKey",
      "@type": "rdfs:Literal"
    },
    "influenced": {
      "@id": "prov:influenced",
      "@type": "@id"
    },
    "qualifiedPrimarySource": {
      "@id": "prov:qualifiedPrimarySource",
      "@type": "@id"
    },
    "qualifiedQuotation": {
      "@id": "prov:qualifiedQuotation",
      "@type": "@id"
    },
    "qualifiedRevision": {
      "@id": "prov:qualifiedRevision",
      "@type": "@id"
    },
    "has_anchor": {
      "@id": "prov:has_anchor",
      "@type": "@id"
    },
    "has_query_service": {
      "@id": "prov:has_query_service",
      "@type": "@id"
    },
    "describesService": {
      "@id": "prov:describesService",
      "@type": "@id"
    },
    "pingback": {
      "@id": "prov:pingback",
      "@type": "@id"
    },
    "dictionary": {
      "@id": "prov:dictionary",
      "@type": "@id"
    },
    "derivedByInsertionFrom": {
      "@id": "prov:derivedByInsertionFrom",
      "@type": "@id"
    },
    "derivedByRemovalFrom": {
      "@id": "prov:derivedByRemovalFrom",
      "@type": "@id"
    },
    "insertedKeyEntityPair": {
      "@id": "prov:insertedKeyEntityPair",
      "@type": "@id"
    },
    "hadDictionaryMember": {
      "@id": "prov:hadDictionaryMember",
      "@type": "@id"
    },
    "pairEntity": {
      "@id": "prov:pairEntity",
      "@type": "@id"
    },
    "qualifiedInsertion": {
      "@id": "prov:qualifiedInsertion",
      "@type": "@id"
    },
    "qualifiedRemoval": {
      "@id": "prov:qualifiedRemoval",
      "@type": "@id"
    },
    "asInBundle": {
      "@id": "prov:asInBundle",
      "@type": "@id"
    },
    "mentionOf": {
      "@id": "prov:mentionOf",
      "@type": "@id"
    },
    "title": "dct:title",
    "description": "dct:description",
    "license": {
      "@id": "dct:license",
      "@type": "@id",
      "@context": {
        "@base": "http://purl.org/NET/rdflicense/"
      }
    },
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "oa": "http://www.w3.org/ns/oa#",
    "rdflicense": "http://purl.org/NET/rdflicense/",
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://raw.githubusercontent.com/ogcincubator/usage-licensing/undefined/build/annotated/usage-project/licensing/prov/context.jsonld)

## Sources

* [Provenance Chain building block](https://ogcincubator.github.io/bblock-prov-schema/bblock/ogc.ogc-utils.prov/)
* [PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/usage-licensing](https://github.com/ogcincubator/usage-licensing)
* Path: `_sources/prov`

