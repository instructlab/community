# Welcome to the InstructLab Community repository🔬

The mission of the InstructLab (**L**arge-scale **A**lignment for chat**B**ots) project is to leverage innovative techniques that overcome challenges in Large Language Model (LLM) training. InstructLab uses a taxonomy based curation process, along with synthetic data generation, that allows the open source community to submit contributions to existing LLMs in an accessible way. 

This repository shares InstructLab's activity and collaboration details across the community. The most current information is included throughout this repository. Contributing issues/pull requests are more than welcome to help us maintain this information.

Related repositories include: 
- [CLI](https://github.com/instruct-lab/cli)
- [Taxonomy](https://github.com/instruct-lab/taxonomy)

## Community Goals 
The goals of this open-source community includes the following:

- Drive adoption of the InstructLab tooling and model API standard.
- Grow an ecosystem of open data (contributions) and open models (interactions).
- Establish deployable patterns, practices, and evidence for sophisticated use cases.

## Getting Started with the InstructLab Project workstreams🥼

InstructLab (**L**arge-scale **A**lignment for chat**B**ots) is an open-source initiative by Red Hat and IBM. It provides a platform for easy engagement with Large Language Models (LLM) by using the `ilab` command-line interface (CLI) tool. Users can augment the LLM’s capabilities by submitting the skills and knowledge that they have tested to the project’s taxonomy repository on GitHub by creating a pull request.

The following documentation shows you an overview of the workflow, and the resources needed, to get started with InstructLab.

## 💻 InstructLab (`ilab`) Workflow 
### Installing and interacting with the `ilab` CLI tool

The `ilab` tool allows you to interact with the IBM AI model `Merlinite`, contribute your own information, and train the model locally. 

1. Navigate to the `ilab` CLI repository and follow the instructions in the [README.md](https://github.com/instruct-lab/cli/blob/main/README.md). The README.md instructs you on how to perform the following: 

    a. In the [Getting started](https://github.com/instruct-lab/cli/blob/main/README.md#-getting-started) section of the README.md file, you can install the `ilab` tool, set up your local environment, and download the IBM `Merlinite` AI model.

    b. You can then create your own data sets to feed into and train the model. In the taxonomy project, there are two types of data you can serve to the model: skills and knowledge. There are a few different types of skills and knowledge you can create. For more detailed information on the types, see the Taxonomy [README.md](https://github.com/instruct-lab/taxonomy/blob/main/README.md#getting-started-with-skill-contributions). 

    c. In your local taxonomy repository, generated after the [Initialize lab](https://github.com/instruct-lab/cli/blob/main/README.md#%EF%B8%8F-initialize-lab) step, navigate to the path that you want to add information to. You can see a flow chart of the paths in this file [taxonomy_diagram](https://github.com/instruct-lab/taxonomy/blob/main/docs/taxonomy_diagram.png). Create a `qna.yaml` file in that path with your contributions. 

    d. [Serve and train the model](https://github.com/instruct-lab/cli/blob/main/README.md#-train-the-model) with your contributions to see if the model can answer questions more accurately. 

    e. Congratulations! You trained an AI model locally! 

### Opening a pull request in the taxonomy repository with your new skills or knowledge! 

If your contributions improved the model locally, you can contribute your files to the main AI model through the taxonomy repository. For more information see [CONTRIBUTING.md](https://github.com/instruct-lab/taxonomy/blob/main/CONTRIBUTING.md#pr-review) in the taxonomy repository.

1. To contribute your knowledge and skills to the taxonomy repository, follow the documentation in [Contribute knowledge and skills to the taxonomy](https://github.com/instruct-lab/taxonomy/blob/main/README.md#contribute-knowledge-and-skills-to-the-taxonomy). 

    > **IMPORTANT:** Ensure that your files and contributions follow the proper YAML format, see examples in the [YAML format](https://github.com/instruct-lab/taxonomy/blob/main/README.md#yaml-format) file.

### Getting reviews on pull requests

There are teams of contributors from Red Hat and IBM that will review your pull request and determine if it can be merged in the taxonomy repository. For more information, see the [Triaging skills](https://github.com/instruct-lab/taxonomy/blob/main/docs/skills-triage.md) documentation. 

### See your contributions impact an AI model!

The IBM model `Merlinite` builds regularly. Sometime after your pull request is merged, Merlinite is updated and you can see locally that the model improved with the skill or knowledge you taught it.

## Governance & Legal
- [InstructLab Community Governance](governance.md)
- [InstructLab Code of Conduct](https://github.com/instruct-lab/community/tree/main?tab=coc-ov-file)
- You must agree to the terms of [Developer Certificate of Origin](https://developercertificate.org/) by signing off your commits in your pull requests. 

The Developer Certificate of Origin (DCO) is a lightweight way for contributors to certify that they wrote or otherwise have the right to submit the code they are contributing to the project. Here is the full [text of the DCO](https://developercertificate.org/), reformatted for readability:

> By making a contribution to this project, I certify that:
>
> a. The contribution was created in whole or in part by me and I have the right to submit it under the open source license indicated in the file; or
>
> b. The contribution is based upon previous work that, to the best of my knowledge, is covered under an appropriate open source license and I have the right under that license to submit that work with modifications, whether created in whole or in part by me, under the same open source license (unless I am permitted to submit under a different license), as indicated in the file; or
>
> c. The contribution was provided directly to me by some other person who certified (a), (b) or (c) and I have not modified it.
>
> d. I understand and agree that this project and the contribution are public and that a record of the contribution (including all personal information I submit with it, including my sign-off) is maintained indefinitely and may be redistributed consistent with this project or the open source license(s) involved.
Contributors _sign-off_ that they adhere to these requirements by adding a `Signed-off-by` line to commit messages.

## Contribution
We encourage contribution in the form of pull requests or comments on existing pull requests. For more information, see 
- [Project Contribution Guidelines](https://github.com/instruct-lab/community/blob/main/CONTRIBUTING.md)
- [Taxonomy's contribution guide](https://github.com/instruct-lab/taxonomy/blob/main/CONTRIBUTING.md)
- [CLI's contribution guide](https://github.com/instruct-lab/cli/blob/main/CONTRIBUTING/CONTRIBUTING.md)

### Contributor Ladder
The project welcomes new contributors. Not all contributors are able to provide sustained contributions, but they are always welcome. [The Contributor Ladder](https://github.com/instruct-lab/community/blob/main/CONTRIBUTOR_LADDER.md) outlines the various roles to support contributors to grow responsibility in the various InstructLab projects.

### Maintainers
To see all maintainers and triagers for InstructLab, see the [Maintainers](https://github.com/instruct-lab/community/blob/main/MAINTAINERS.md) file.

## Information resources
- [InstructLab Slack]() FORTHCOMING
- [InstructLab Mailing lists]() FORTHCOMING
- In the meantime, feel free to start a [discussion](https://github.com/orgs/instruct-lab/discussions).
  
## Licenses

Distributed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

SPDX-License-Identifier: [Apache-2.0](https://spdx.org/licenses/Apache-2.0)

If you would like to see the detailed LICENSE click [here](LICENSE).

## Quick Links
* [LICENSE](LICENSE)
* [README](README.md)
* [CONTRIBUTING](CONTRIBUTING.md)
* [MAINTAINERS](MAINTAINERS.md)
* [SECURITY](SECURITY.md)
* [CHANGELOG](CHANGELOG.md)
