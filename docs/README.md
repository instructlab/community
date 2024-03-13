# InstructLab Community Learning Guide

InstructLab crowd sources the process of tuning and improving models by collecting two types of data, knowledge and skills. These submissions are collected in a taxonomy of YAML files to be used in the synthetic data generation process.

![Overview of the LAB alignment method. From Sudalairaj et al., 2 Mar 2024.](taxonomy_paper_diagram.png)

At this time, the InstructLab taxonomy is accepting Skills submissions only.

## Learning Topics

* [Skills Guide](./SKILLS_GUIDE.md)
* [Knowledge Guide](./KNOWLEDGE_GUIDE.md)

## License Limitations

If you would like to contribute any third-party data to either the Skills or Knowledge taxonomies, you must ensure the license on the data is unrestricted for commercial use.

This applies to:

* data embedded in `.md` files as knowledge
* data offered as `context` in `qna.yaml` files for skills
* questions and answers sourced from elsewhere and used as `qna.yaml` submissions

The following licenses are permitted:

* CC0: Same as public domain
* CDLA-Permissive (any version, version 2.0 preferred)
* CC BY 4.0 (requires only Attribution)
* CC-BY-SA-4.0
* Apache 2.0
* MIT
* Other open data licenses that do not restrict commercial use or creation of derivative works (including the creation of verbatim copies, aka sharing)

## Avoid These Topics

While the tuning process may eventually benefit from being used to help the models work with complex social topics, at this time this is an area of active research we do not want to take lightly. Therefore please keep your submissions clear of the following topics:

* Religion
* Politics - history is fine but current politics
* PII
* Violence
* Cyber Bullying
* Internal docs
* Discrimination
* Medical info
* Legal settlements/mitigations
* Gender Bias
* Hostile Language, threats, slurs, derogatory or insensitive jokes or comments
* Pornography
