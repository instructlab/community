# Welcome to the Lab 🔬

![image](https://github.com/instruct-lab/community/assets/85503753/25fcefc7-a7ac-4511-90df-dc397ba741d5)

## Why InstructLab
There are many projects rapidly embracing and extending permissively licensed AI models, but they are faced with three main challenges:
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

---

# InstructLab is composed of the following projects:

## [Taxonomy](https://github.com/instruct-lab/taxonomy)

The InstructLab method is driven by taxonomies, which are largely created manually and with care. This repository contains a taxonomy tree that will allow you to create models tuned with your data (enhanced via synthetic data generation) using the InstructLab method.

- [Repo]()
- [Contributing]()

## [Command-line Interface](https://github.com/instruct-lab/cli)

This command-line interface for InstructLab will allow you to create models tuned with data you provide using the InstructLab method on your laptop or workstation.

- [Repo]()
- [Contributing]()
  
## Model Training Infrastructure

The infrastructure used to regularly train the model based on new contributions from the community is GPU intensive and generously donated and maintained by IBM.

---

## Additonal aspects of the project include:

- [community](): community content
- [github-bots](): automated CI/CD bots and related content


### Code of Conduct & Covenant
Participation in the InstructLab community is governed by our [Code of Conduct & Covenant](https://github.com/instruct-lab/community/blob/main/CODE_OF_CONDUCT.md).

### Governance
How the InstructLab project [governance](https://github.com/instruct-lab/community/blob/main/governance.md) operates.

### Security
Security policies and practices, including reporting vulnerabilities can be found in our [Security.md](https://github.com/instruct-lab/community/blob/main/SECURITY.md).
