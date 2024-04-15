# InstructLab Community Learning Guide

InstructLab crowd sources the process of tuning and improving models by collecting two types of data, knowledge and skills. These submissions are collected in a taxonomy of YAML files to be used in the synthetic data generation process.

![Overview of the LAB alignment method. From Sudalairaj et al., 2 Mar 2024.](taxonomy_paper_diagram.png)

We accept contributions of both Skills and Knowledge to InstructLab.

## Learning Topics

* [Skills Guide](https://github.com/instruct-lab/taxonomy/blob/main/README.md#getting-started-with-skill-contributions)
* [Knowledge Guide](https://github.com/instruct-lab/taxonomy/blob/main/README.md#getting-started-with-knowledge-contributions)

## License Limitations

If you would like to contribute any third-party data to either the Skills or Knowledge taxonomies, you must ensure the license on the data is unrestricted for commercial use.

This applies to:

* data embedded in `.md` files as knowledge
* data offered as `context` in `qna.yaml` files for skills
* questions and answers sourced from elsewhere and used as `qna.yaml` submissions

For this project, unless the file says otherwise, or unless the attributed source provided in the file says otherwise, the relevant open source license is the Apache License, Version 2.0. All contributions that leverage third party content should either come from the public domain (e.g. out of copyright, or .gov sites) or be licensed with an open data license that does not restrict commercial use or the creation of derivative works, including the following license types:
- CC0
- CDLA-Permissive-2.0
- CC-BY-4.0
- Apache 2.0
- MIT

Any third party content contributed to this project undergoes modifications in order to formulate it in the templated format required for submission to this project.

## Avoid These Topics

While the tuning process may eventually benefit from being used to help the models work with complex social topics, at this time this is an area of active research we do not want to take lightly. Therefore please keep your submissions clear of the following topics:

* PII (personally identifiable information) or any content invasive of individual privacy rights
* Violence including self-harm
* Cyber Bullying
* Internal documentation or other that is confidential to your employer or organization, e.g. trade secrets
* Discrimination
* Religion
  * Facts such as, "[Christianity is, according to the 2011 census, the fifth most practiced religion in Nepal, with 375,699 adherents, or 1.4% of the population.](https://en.wikipedia.org/wiki/Christianity_in_Nepal)", are fine as a knowledge contribution. Advocating in favor of or against any religious faith is not acceptable.
* Medical or health information
  * Facts such as,  "[In mammals, pulmonary ventilation occurs via inhalation (breathing)](https://opentextbc.ca/biology/chapter/11-3-circulatory-and-respiratory-systems/)," are fine as a knowledge contribution. Tailored medical/health advice is not acceptable.
* Financial information
  * Facts such as "[laissez-faire economics ... argues that market forces alone should drive the economy and that governments should refrain from direct intervention in or moderation of the economic system](https://openstax.org/books/world-history-volume-2/pages/6-3-capitalism-and-the-first-industrial-revolution)," are fine as a knowledge contribution. Tailored financial advice is not acceptable.
* Legal settlements/mitigations
* Gender Bias
* Hostile Language, threats, slurs, derogatory or insensitive jokes or comments
* Profanity
* Pornography and sexually explicit or suggestive content
* Any contributions that would allow for automated decision making that affect an invidual's rights or well-being, e.g. social scoring
* Any contributions that engage in political campaigning or lobbying
* Jokes
* Poems

## Works Cited on this Page
* [Concepts of Biology - 1st Canadian Edition](https://opentextbc.ca/biology/), Chapter 11.3 _Circulatory and Respiratory Systems_. Copyright 2015 by Charles Molnar and Jane Gair, licensed under a [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/). No modications were made to the text.
* [World History, volume 2: from 1400](https://openstax.org/details/books/world-history-volume-2), Chapter 6.3 _Capitalism and the First Industrial Revolution_. Copyright 2022 Rice University, licensed under a [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/). No modications were made to the text.
