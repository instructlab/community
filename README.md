# Welcome to the InstructLab Community repository🔬

The mission of the InstructLab (**L**arge-scale **A**lignment for chat**B**ots) project is to leverage innovative techniques that overcome challenges in Large Language Model (LLM) training. InstructLab uses a taxonomy based curation process, along with synthetic data generation, that allows the open source community to submit contributions to existing LLMs in an accessible way.

InstructLab is made up of several projects that are defined as codebases and services with different release cycles. Collectively, these enable large-model development. This repository shares InstructLab's activity and collaboration details across the community and include the most current information about the project. Related repositories include the following:

* [taxonomy tree](https://github.com/instructlab/taxonomy) of knowledge and skills.
* [ilab](https://github.com/instructlab/instructlab) command-line interface (CLI) tool for model [fine-tuning](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)).

Contributing new features, resolving bugs and issues, and refining the documentation experience through pull requests are welcome. More information about contributing to the InstructLab Project, contributor roles, governance and legal, and licenses can be found in proceeding sections of this document.

## Community Goals

The goals of this open source community includes the following:

* Drive adoption of the InstructLab tooling and model API standard.
* Grow an ecosystem of contribution driven open models
* Establish deployable patterns, practices, and evidence for sophisticated use cases.

## Project Communication Channels

There are many ways to engage with InstructLab project maintainers and community members outside of GitHub. You can find all of these, including timing for our community meetings and office hours, on our [Collaboration page](https://github.com/instructlab/community/blob/main/Collaboration.md).

## Getting Started with the InstructLab Project workstreams🥼

InstructLab (**L**arge-scale **A**lignment for chat**B**ots) is an open source initiative by Red Hat and IBM. It provides a platform for easy engagement with Large Language Models (LLM) by using the `ilab` command-line interface (CLI) tool. Users can augment the LLM's capabilities by submitting the skills and knowledge that they have tested to the project’s taxonomy repository on GitHub by creating a pull request.

The following documentation shows you an overview of the workflow, and the resources needed, to get started with InstructLab.

## 💻 InstructLab (`ilab`) Workflow

### Installing and interacting with the `ilab` CLI tool

The `ilab` tool allows you to interact with the IBM AI model `Merlinite` or `Granite`, contribute your own information, and train the model locally.

> **Note:** Before proceeding, it might be beneficial to check out the [Contributing](https://github.com/instruct-lab/community/blob/main/CONTRIBUTING.md) guide for an overview of contributing practices and expectations. Additionally, you should consider joining the [InstructLab community Slack channel](https://github.com/instructlab/community/blob/main/InstructLab_SLACK_GUIDE.md).

1. Navigate to the `ilab` CLI repository and follow the instructions in the [README.md](https://github.com/instructlab/instructlab/blob/main/README.md). The README.md instructs you on how to perform the following:

    a. In the [Getting started](https://github.com/instructlab/instructlab/blob/main/README.md#-getting-started) section of the README.md file, you can install the `ilab` tool, set up your local environment, and download the IBM Merlinite-7b (default) AI model. If you run into any issues, you can find many solutions in the [in the CLI repository's discussion board](https://github.com/instructlab/instructlab/discussions).

    b. You can then create your own data sets to feed into and train the model. In the taxonomy project, there are two types of data you can serve to the model: skills and knowledge. There are a few different types of skills and knowledge you can create. For more detailed information on the types, see the Taxonomy [README.md](https://github.com/instructlab/taxonomy/blob/main/README.md#welcome-to-the-instructlab-taxonomy).

    c. In your local taxonomy repository, generated after the [Initialize ilab](https://github.com/instructlab/instructlab/blob/main/README.md#%EF%B8%8F-initialize-ilab) step, navigate to the path that you want to add information to.
    You can see a flow chart of the paths in this file [taxonomy_diagram](https://github.com/instructlab/taxonomy/blob/main/docs/taxonomy_diagram.md).
    Create a `qna.yaml` file in that path with your contributions.

    d. [Serve and train the model](https://github.com/instructlab/instructlab/blob/main/README.md#-train-the-model) with your contributions to see if the model can answer questions more accurately.

    e. Congratulations! You trained an AI model locally!

### Opening a pull request in the taxonomy repository with your new skills or knowledge

If your contributions improved the model locally, you can contribute your files to the main AI model through the taxonomy repository. For more information see [CONTRIBUTING.md](https://github.com/instructlab/taxonomy/blob/main/CONTRIBUTING.md#pull-request-review) in the taxonomy repository.

1. To contribute your knowledge and skills to the taxonomy repository, follow the documentation in [Contribute knowledge and skills to the taxonomy](https://github.com/instructlab/taxonomy/blob/main/README.md#contribute-knowledge-and-skills-to-the-taxonomy).

    > **IMPORTANT:** Ensure that your files and contributions follow the proper YAML format, see examples in the [Skills: YAML format](https://github.com/instructlab/taxonomy/blob/main/README.md#skills-yaml-examples) file.

### Getting reviews on pull requests

There are teams of contributors from Red Hat and IBM that will review your pull request and determine if it can be merged in the taxonomy repository. For more information, see the [Triaging contributions](https://github.com/instructlab/taxonomy/blob/main/docs/triaging/triaging-contributions.md) documentation.

### See your contributions impact an AI model

The Merlinite-7b and Granite-7b models are built regularly. Sometime after your pull request is merged, Merlinite is updated and you can see locally that the model improved with the skill or knowledge you taught it.

## Contribution

Help on open source projects is always welcome and there is always something that can be improved. For example, documentation (like the text you are reading now) can always use improvement, code can always be clarified, variables or functions can always be renamed or commented on, and there is always a need for more test coverage. If you see something that you think should be fixed, take ownership!

To contribute code or documentation, please submit a pull request to the relevant repository. Note that contribution to any repository has its own set of requirements and expectations, and users should familiar themselves with those expectations before contributing.

* For more information about general contribution practices, see the [Contributing](https://github.com/instructlab/community/blob/main/CONTRIBUTING.md) guide.
* For more information about contributing to the taxonomy repository, see the [Taxonomy's contribution guide](https://github.com/instructlab/taxonomy/blob/main/CONTRIBUTING.md).
* For more information about contributing to the InstructLab CLI repository, see the [InstructLab contribution guide](https://github.com/instructlab/instructlab/blob/main/CONTRIBUTING/CONTRIBUTING.md).

### Contributor roles

The project welcomes new contributors. Not all contributors are able to provide sustained contributions, but they are always welcome. [The contributor roles](https://github.com/instructlab/community/blob/main/CONTRIBUTOR_ROLES.md) document outlines the various roles to support contributors and help them grow responsibility in the various InstructLab projects. These roles are subject to change, and new roles will be added as necessary.

#### Maintainers

Project Maintainers are first and foremost contributors that have shown they are committed to the long term success of a project. Maintainership is about building trust with the community and being a person that everyone can depend on to make consistent decisions in the best interest of the project. With enough time and experience, contributors can apply to become Maintainers. The current list of Maintainers can be found in the
[Maintainers](https://github.com/instructlab/community/blob/main/MAINTAINERS.md) file.

## Governance & Legal

* [InstructLab Community Governance](GOVERNANCE.md)

* [InstructLab Code of Conduct](CODE_OF_CONDUCT.md)

* You must agree to the terms of the [Developer Certificate of Origin (DCO)](https://developercertificate.org/) by signing off your commits in your pull requests. The Developer Certificate of Origin (DCO) is a lightweight way for contributors to certify that they wrote or otherwise have the right to submit the code they are contributing to the project. Here is the full [text of the DCO](https://developercertificate.org/), reformatted for readability:

  > By making a contribution to this project, I certify that:
  >
  > a. The contribution was created in whole or in part by me and I have the right to submit it under the open source license indicated in the file; or
  >
  > b. The contribution is based upon previous work that, to the best of my knowledge, is covered under an appropriate open source license and I have the right under that license to submit that work with modifications, whether created in whole or in part by me, under the same open source license (unless I am permitted to submit under a different license), as indicated in the file; or
  >
  > c. The contribution was provided directly to me by some other person who certified (a), (b) or (c) and I have not modified it.
  >
  > d. I understand and agree that this project and the contribution are public and that a record of the contribution (including all personal information I submit with it, including my sign-off) is maintained indefinitely and may be redistributed consistent with this project or the open source license(s) involved.

Contributors _sign-off_ that they adhere to these requirements by adding a `Signed-off-by` line to commit messages. For more information about how the DCO works with this project, see [Developer Certificate of Origin (DCO)](https://github.com/instructlab/community/blob/main/CONTRIBUTING.md#developer-certificate-of-origin-dco).

## Licenses

Distributed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

SPDX-License-Identifier: [Apache-2.0](https://spdx.org/licenses/Apache-2.0)

If you would like to see the detailed LICENSE click, see [LICENSE](LICENSE).

## Contact resources

* [InstructLab Slack](https://instruct-lab.slack.com). See the InstructLab Slack Guide for directions on how to join.
* [InstructLab Slack Guide](InstructLab_SLACK_GUIDE.md)
* [InstructLab Slack Moderation Guide](InstructLabSlackModerationGuide.md)
* [InstructLab Mailing lists](https://github.com/instructlab/community/blob/main/Collaboration.md#aliases-and-mailing-lists-catalog)
* [Discussion](https://github.com/orgs/instructlab/discussions).

## Quick Links

* [FAQ](FAQ.md)
* [LICENSE](LICENSE)
* [README](README.md)
* [CONTRIBUTING](CONTRIBUTING.md)
* [MAINTAINERS](MAINTAINERS.md)
* [SECURITY](SECURITY.md)
* [CHANGELOG](CHANGELOG.md)
