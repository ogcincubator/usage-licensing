
# ODRL 2.2 Action (Schema)

`eu.usage-project.licensing.odrl.2.2.action` *v0.1*

An Action according to the Open Digital Rights Language (ODRL) version 2.2.

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$defs:
  actionObject:
    type: object
    properties:
      uid:
        type: string
        x-jsonld-id: rdf:value
        x-jsonld-type: '@id'
      refinement:
        oneOf:
        - $ref: https://raw.githubusercontent.com/ogcincubator/usage-licensing/undefined/build/annotated/usage-project/licensing/odrl/2/2/constraint/schema.yaml
        - type: array
          items:
            $ref: https://raw.githubusercontent.com/ogcincubator/usage-licensing/undefined/build/annotated/usage-project/licensing/odrl/2/2/constraint/schema.yaml
oneOf:
- type: string
- type: array
  items:
    type: string
- $ref: '#/$defs/actionObject'
- type: array
  items:
    $ref: '#/$defs/actionObject'

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/ogcincubator/usage-licensing/undefined/build/annotated/usage-project/licensing/odrl/2/2/action/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/ogcincubator/usage-licensing/undefined/build/annotated/usage-project/licensing/odrl/2/2/action/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "uid": {
      "@id": "rdf:value",
      "@type": "@id"
    },
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://raw.githubusercontent.com/ogcincubator/usage-licensing/undefined/build/annotated/usage-project/licensing/odrl/2/2/action/context.jsonld)

## Sources

* [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/usage-licensing](https://github.com/ogcincubator/usage-licensing)
* Path: `_sources/odrl/2.2/action`

