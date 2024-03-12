<!-- This should be the location of the title of the repository, normally the short name -->
# Welcome to the Lab 🔬
There is a great need for rapid innovation on open models.
Cue open source AI. 

![image](https://github.com/instruct-lab/community/assets/85503753/25fcefc7-a7ac-4511-90df-dc397ba741d5)

## Why InstructLab
AI becomes stronger, more stable and secure with an open approach to large model development.There are many projects rapidly embracing and extending permissively licensed AI models, but they are faced with three main challenges:
* Contribution to the models themselves is not possible directly.  They show up as forks, which forces consumers to choose a “best-fit” model that isn’t easily extensible, and the forks are expensive for model creators to maintain.
* The ability to contribute ideas is limited by a lack of AI/ML expertise.  One has to learn how to fork, train, and refine models in order to see their idea move forward.  This is a very high barrier to entry.
* There is no direct community governance or best practice around review, curation, and distribution of forked models.

## Unforking Models: The InstructLab Method
IBM and Red Hat are working on a project that allows the establishment of a pull request-like upstream contribution acceptance workflow for models. These upstream contributions add additional "skills" or "knowledge" to the model. These skills can be built by providing a much smaller number of "example" data artifacts than would normally be required to influence an LLM. (E.g., 3 sample documents instead of 5,000.) The technique involves using generative AI to create synthetic data to "expand" the limited data artifact set to a scale that would influence the model. This generated data is then used in a training step, effectively teaching it a new skill that it previously could not do, or did not do well.  This skill can then be submitted upstream to the model, and if accepted, the model would not need to be rebuilt entirely, but the skill would be included by being built on top as a layer composed on top.

A model would then include a "tree of skills" (taxonomy) composed on top.

The way this technology has been built, it is not model-specific, so it could apply as easily to say the llama family of models as the IBM granite family. There is a potential to onboard other model creators (e.g. Mistral, Meta, etc.) as partners in following this approach to accepting upstream contributions back into the models. IBM has already released two "lab-enhanced" (via InstructLab) models on HuggingFace in the past week:

[Labradorite](https://huggingface.co/ibm/labradorite-13b) (lab-enhanced llama2)
[Merlinite](https://huggingface.co/ibm/merlinite-7b) (lab-enhanced Mistral)

The technology gives model upstreams with sufficient infrastructure resources (e.g. IBM) the ability to create nightly builds of their open source licensed models (again, not rebuilding / retraining the entire model, but composing just the new skills into it.) They would accept pull requests to their models; these PRs would then be included in the next nightly build.

Contributors that are currently creating their own forks of models like Mistral would be able to accelerate their work and avoid the costs of forking and retraining their models.  Once proven out, we expect this to attract an even broader set of contributors that have less AI expertise but have creative ideas on how to extend AI models.



## Technical Overview
InstructLab is an automated instruction-based model tuning method and toolset that accelerates and standardized model knowledge and skill composition and alignment to instruction following. It utilizes a model content and prompt behavior configuration standard to specify, and then generate and refine synthetic training data and deploy it through a novel training method. This process enables adding user-specified knowledge and skills (a “model pull request”) to various open model baselines, and merge various pull requests (model “merge”) into a single model. It also results in standardized and predictable prompting behavior even as the model content and alignment changes, Tests today have demonstrated rapid cycles of progress with small teams (~few developers) updating various open models with new skills and higher accuracy benchmarking (e.g. MT Bench). 


## Community Goals
This open-source community effort must accomplish, at least, the following goals:
* Build out, validate, and drive adoption of the InstructLab tooling and model API standard.
* Grow ecosystem of open data (inputs) and open models (outputs) as enablers and proof points.
* Establish deployable app patterns, practices and proof points for sophisticated use cases.


## Usage

* [LICENSE](LICENSE)
* [README.md](README.md)
* [CONTRIBUTING.md](CONTRIBUTING.md)
* [MAINTAINERS.md](MAINTAINERS.md)
* [CHANGELOG.md](CHANGELOG.md)


## Legal & Governance
- [InstructLab Community Governance](governance.md)
- [InstructLab Code of Conduct](https://github.com/instruct-lab/community/tree/main?tab=coc-ov-file)


## Resources
- [InstructLab Website]()
- [InstructLab Mailing lists]()



<!-- Questions can be useful but optional, this gives you a place to say, "This is how to contact this project maintainers or create PRs -->
If you have any questions or issues you can create a new [issue here](https://github.com/instruct-lab/community/issues).

Pull requests are very welcome! Make sure your patches are well tested.
Ideally create a topic branch for every separate change you make. For
example:

1. Fork the repo
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## License

Distributed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

SPDX-License-Identifier: [Apache-2.0](https://spdx.org/licenses/Apache-2.0)

If you would like to see the detailed LICENSE click [here](LICENSE).



