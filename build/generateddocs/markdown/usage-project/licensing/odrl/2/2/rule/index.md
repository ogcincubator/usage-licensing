
# ODRL 2.2 Rule (Schema)

`eu.usage-project.licensing.odrl.2.2.rule` *v0.1*

A Rule according to the Open Digital Rights Language (ODRL) version 2.2

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$defs:
  rule:
    type: object
    required:
    - action
    action:
      $ref: '#/$defs/action'
    duty:
      $ref: '#/$defs/rule'
    remedy:
      $ref: '#/$defs/rule'
    target:
      oneOf:
      - type: string
      - type: object
  action:
    oneOf:
    - type: string
    - type: array
      minItems: 1
      items:
        type: string
$ref: '#/$defs/rule'
x-jsonld-extra-terms:
  Action: odrl:Action
  action:
    x-jsonld-type: '@vocab'
    x-jsonld-id: odrl:action
  Duty: odrl:Duty
  duty:
    x-jsonld-type: '@id'
    x-jsonld-id: odrl:duty
  consequence:
    x-jsonld-type: '@id'
    x-jsonld-id: odrl:consequence
  remedy:
    x-jsonld-type: '@id'
    x-jsonld-id: odrl:remedy
  target:
    x-jsonld-type: '@id'
    x-jsonld-id: odrl:target

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/ogcincubator/usage-licensing/undefined/build/annotated/usage-project/licensing/odrl/2/2/rule/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/ogcincubator/usage-licensing/undefined/build/annotated/usage-project/licensing/odrl/2/2/rule/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "Action": "odrl:Action",
    "action": {
      "@type": "@vocab",
      "@id": "odrl:action"
    },
    "Duty": "odrl:Duty",
    "duty": {
      "@type": "@id",
      "@id": "odrl:duty"
    },
    "consequence": {
      "@type": "@id",
      "@id": "odrl:consequence"
    },
    "remedy": {
      "@type": "@id",
      "@id": "odrl:remedy"
    },
    "target": {
      "@type": "@id",
      "@id": "odrl:target"
    },
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://raw.githubusercontent.com/ogcincubator/usage-licensing/undefined/build/annotated/usage-project/licensing/odrl/2/2/rule/context.jsonld)

## Sources

* [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/usage-licensing](https://github.com/ogcincubator/usage-licensing)
* Path: `_sources/odrl/2.2/rule`

