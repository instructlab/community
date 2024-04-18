# InstructLab FAQ

Last updated: April 2024

# Table of Contents

- [Document summary](#document-summary)
- [General FAQ](#general-faq)
  - [What is InstructLab?](#what-is-instructlab)
  - [What is LAB?](#what-is-lab)
  - [How does InstructLab work?](#how-does-instructlab-work)
  - [What are the goals of the InstructLab project?](#what-are-the-goals-of-the-instructlab-project)
  - [How can I contribute?](#how-can-i-contribute)
  - [I'm having problems with the `ilab` CLI tool. What should I do?](#im-having-problems-with-the-ilab-cli-tool-what-should-i-do)
  - [Why should I contribute?](#why-should-i-contribute)
  - [What large language models (LLMs) am I contributing to through the InstructLab project?](#what-large-language-models-llms-am-i-contributing-to-through-the-instructlab-project)
  - [What is Merlinite-7b?](#what-is-merlinite-7b)
  - [What is a “skill”?](#what-is-a-skill)
  - [What is “knowledge”?](#what-is-knowledge)
  - [Is the project looking for certain types of skill contributions?](#is-the-project-looking-for-certain-types-of-skill-contributions)
  - [What are the acceptance criteria for a skills submission?](#what-are-the-acceptance-criteria-for-a-skills-submission)
  - [What are the acceptance criteria for a knowledge submission?](#what-are-the-acceptance-criteria-for-a-knowledge-submission)
  - [How can I submit a skill or knowledge?](#how-can-i-submit-a-skill-or-knowledge)
  - [What happens after you submit a pull request?](#what-happens-after-you-submit-a-pull-request)
  - [How are submissions reviewed?](#how-are-submissions-reviewed)
  - [How long will it take for my pull request to be reviewed?](#how-long-will-it-take-for-my-pull-request-to-be-reviewed)
  - [If my pull request is accepted, how long will it take for my changes to appear in the next model update?](#if-my-pull-request-is-accepted-how-long-will-it-take-for-my-changes-to-appear-in-the-next-model-update)
  - [What is the software license for InstructLab?](#what-is-the-software-license-for-instructlab)
  - [Am I required to license code submissions to InstructLab under the Apache 2.0 license?](#am-i-required-to-license-code-submissions-to-instructlab-under-the-apache-20-license)
  - [My contribution requires submitting data along with code. What data is permissible to include?](#my-contribution-requires-submitting-data-along-with-code-what-data-is-permissible-to-include)
  - [Where can I download updated models of InstructLab?](#where-can-i-download-updated-models-of-instructlab)
  - [I have a question about the project. Where should I go?](#i-have-a-question-about-the-project-where-should-i-go)
  - [What are the software and hardware requirements for using InstructLab?](#what-are-the-software-and-hardware-requirements-for-using-instructlab)
- [Additional Resources](#additional-resources)

## Document summary

This page serves as a comprehensive FAQ for the InstructLab project, detailing how it works, how to begin contribution, and the goals behind the project. Key information includes:

* **InstructLab Overview**: This open source project allows users to interact with and train the Merlinite-7b AI Large Language Model (LLM) by contributing skills and knowledge.
* **LAB Method**: A synthetic data-based tuning method for LLMs consisting of a taxonomy-driven data curation process, a synthetic data generator, and two-phased training with replay buffers.
* **Contribution Process**: Contributors can add skills or knowledge to the LLM by creating YAML files and testing changes locally before submitting a pull request to InstructLab’s GitHub repository.
* **Project Goals**: To democratize contributions to AI and LLMs, allowing rapid model development through community collaboration facilitated by weekly builds that integrate community contributions.

## Documentation disclaimer

There are currently three repositories that contain documentation crucial to getting users starting with the project:

* [Community](https://github.com/instruct-lab/community) This repository shares InstructLab's activity and collaboration details across the community and include the most current information about the project. It should be approached as the primary repository for getting started, and contains procedures and links to relevant information to make the process as simple as possible.
* [`ilab` command-line interface (CLI) tool](https://github.com/instruct-lab/cli). This repository is responsible for the `ilab` CLI tool. It provides information about how to download the `ilab` CLI, how to contribute to the `ilab` CLI tool, among others.
* [taxonomy tree](https://github.com/instruct-lab/taxonomy). This repository is responsible for the taxonomy tree that allows you to create models tuned with your data. It provides information about what skills and knowledge are, how to create a pull request to contribute to the AI model, and expectations for pull request review. 

As this project grows, documentation and its organization will change. Members of this project will be made aware of significant changes and updates made to documentation.

## General FAQ

### What is InstructLab?

InstructLab (**L**arge-scale **A**lignment for chat**B**ots) is an open source initiative that provides a platform for easy engagement with the Merlinite -7b AI Large Language Model (LLM) by using the `ilab` command-line interface (CLI) tool. You can use the CLI to work with Merlinite-7b to test new skills and knowledge, for example, asking it to write a poem or answer a question about a particular subject. Users can then augment the LLM’s capabilities by submitting the skills and knowledge they have tested to the project’s taxonomy repository on GitHub by creating a pull request. This approach encourages community-driven enhancements without the need for complex model forking or fine-tuning of the model, promoting rapid development through collaborative contributions.

### What is LAB?

LAB (**L**arge-scale **A**lignment for chat**B**ots) is a novel synthetic data-based align tuning method for LLMs from IBM Research. It consists of three components:

1. A taxonomy-drive data curation process
2. A large-scale synthetic data generator
3. Multi-phased-training with replay buffers

The LAB approach allows incrementally adding new knowledge and skills to an already pre-trained model without catastrophic forgetting.

More information about the LAB method can be found on the [Hugging Face project page](https://huggingface.co/ibm/merlinite-7b).

### How does InstructLab work?

InstructLab is driven by taxonomies, or _trees of skills_, and works by empowering users to add new [_skills_ and _knowledge_](https://github.com/instruct-lab/taxonomy/blob/main/README.md#learning) to a pre-trained LLM.

### What are the goals of the InstructLab project?

In its current state, openly contributing to a large language model (LLM) has been difficult because of the large compute infrastructure needed to run one.

The InstructLab project seeks to democratize the contribution to AI and LLMs through its _taxonomy_ repository. When users contribute to the InstructLab project, the taxonomy repository resynthesizes the open source training data for InstructLab-trained LLMs. The model is then re-trained regularly (weekly builds), ensuring that community contributions are integrated while enriching the model’s capabilities over time.

### How can I contribute?

You can begin your contribution journey by reading over the [Contributing](https://github.com/instruct-lab/community/blob/main/CONTRIBUTING.md) guide and joining the [Community Slack Channel](https://join.slack.com/t/instruct-lab/shared_invite/zt-2ginke0oz-SxvNYZCqBTDy5wzAi9WRlA).

When you're ready to start contributing, you can follow the [Getting started](https://github.com/instruct-lab/community/blob/main/README.md#getting-started-with-the-instructlab-project-workstreams) guide. This guide shows you how to

* Install the `ilab` CLI.
* Deploy the LLM locally.
* Add skills or knowledge and train to the local LLM with your data.
* Create a pull request and add your information to the InstructLab taxonomy. 
* Get reviews on your pull requests

### I'm having problems with the `ilab` CLI tool. What should I do?

A list of common problems associated with downloading the `ilab` CLI tool can be found [in the CLI repository's discussion board](https://github.com/instruct-lab/cli/discussions).

### Why should I contribute?

InstructLab is designed to enable collaboration around Merlinite-7b, an open source LLM that contributors can access through [Hugging Face](https://huggingface.co/collections/ibm/large-language-models-65d8bb0fa7d935c9c49b4104). Participating is an opportunity to contribute to open source AI regardless of technical background.

When contributors write an extension to the existing taxonomy, make a pull request, and get it reviewed and merged, their changes are rolled out in the next build. This update strategy expedites the model’s capabilities and allows contributors to see the impact that they have made on the model much sooner than other LLMs.

### What large language models (LLMs) am I contributing to through the InstructLab project?

Contributions to the InstructLab project update Merlinite-7b, an open source LLM. Contributors have direct access to the model they are improving through [Hugging Face](https://huggingface.co/collections/ibm/large-language-models-65d8bb0fa7d935c9c49b4104).

### What is Merlinite-7b?

Merlinite-7b is a Mistral-7b derivative model trained with the LAB (**L**arge-scale **A**lignment for chat**B**ots) using Mixtral-8x7b-Instruct as a teacher model.

More information about the Merlinite-7b can be found on the [Hugging Face project page](https://huggingface.co/collections/ibm/large-language-models-65d8bb0fa7d935c9c49b4104).

### What is a “skill”?

In the context of InstructLab, a [_skill_](https://github.com/instruct-lab/taxonomy/blob/main/README.md#getting-started-with-skill-contributions) is a capability domain submitted by a contributor intending to train the AI model on the submitted information. In other words, when you submit a skill, you teach the AI model _how to do something_.

InstructLab skills are broken down into two main categories:

* [**Composition skills.**](https://github.com/instruct-lab/community/blob/main/docs/SKILLS_GUIDE.md#compositional-skills) Composition or _performative_ skills allow AI models to perform specific tasks or functions. With InstructLab, there are two types of composition skills:
    * [**Freeform compositional skills**](https://github.com/instruct-lab/community/blob/main/docs/SKILLS_GUIDE.md#freeform-compositional-skills) are performative skills that do not require additional context. For example, to train an AI model to write a poem, you would provide examples of poems.
    * [**Grounded compositional skills**](https://github.com/instruct-lab/community/blob/main/docs/SKILLS_GUIDE.md#grounded-compositional-skills) are performative skills that require additional context. One example is how an AI model reads the value of a cell in a table layout. To create the grounded skill to read a table formatted in Markdown, the additional context might be an example table layout.
* **Foundational skills.** Foundational skills are skills like math, reasoning, and coding.
**Note**: Foundational skills are not currently being accepted.


Skills are written in a YAML file and submitted to the InstructLab upstream project for review. See the [Skills: YAML examples](https://github.com/instruct-lab/taxonomy/blob/main/README.md#skills-yaml-examples) for different types of examples. 

### What is “knowledge”?

[_Knowledge_](https://github.com/instruct-lab/taxonomy/blob/main/README.md#getting-started-with-knowledge-contributions) consists of data and facts. When creating knowledge for an AI model, you are providing it with additional data and information to answer questions more accurately. Whereas skills are the information that trains an AI model on how to do something, knowledge is based on the AI model’s ability to answer questions that involve facts, data, or references.

Like skills, knowledge submissions are submitted in YAML format to the InstructLab upstream project for review. See the [Knowledge: YAML examples](https://github.com/instruct-lab/taxonomy/blob/main/README.md#knowledge-yaml-examples) for different types of examples. 

### Is the project looking for certain types of skill contributions?

Currently, InstructLab only accepts compositional (_freeform_ and _grounded_) skills and knowledge. However, any type of freeform or grounded skill can be submitted. Some skills might not be added to the taxonomy repository for reasons such as duplication, submitting a skill that the model already does well, or submitting a controversial skill.

Foundational skills are not currently being accepted.

For a list of accepted skills, see [Accepted Skills](https://github.com/instruct-lab/community/blob/main/docs/SKILLS_GUIDE.md#accepted-skills).

### What are the acceptance criteria for a skills submission?

Skills should seek to add capabilities or a knowledge domain to the AI model; in other words, a skills submission should teach the AI model _how to do something_ instead of providing information _about something_. A good skills submission might address something that the AI model does poorly and seek to enhance its ability to execute that capability better. For a list of commonly accepted skills, see [Accepted Skills](https://github.com/instruct-lab/community/blob/main/docs/SKILLS_GUIDE.md#accepted-skills).

Skills submissions that are unlikely to be accepted include submitting a knowledge request instead of a skills request, submitting a skill that the model already does well, submitting a controversial skill, or submitting skills that do not execute pure math or coding. For a list of skills to avoid submitting, see [Skills to Avoid](https://github.com/instruct-lab/community/blob/main/docs/SKILLS_GUIDE.md#skills-to-avoid).

### What are the acceptance criteria for a knowledge submission?

Requirements for knowledge submissions can be found in the [Getting Started with Knowledge Contributions](https://github.com/instructlab/taxonomy?tab=readme-ov-file#getting-started-with-knowledge-contributions) guide.

### How can I submit a skill or knowledge?

For information about submitting a skill after you have identified a gap, see the [Ways to contribute guide](https://github.com/instruct-lab/taxonomy?tab=readme-ov-file#ways-to-contribute).

### What happens after you submit a pull request?

After a pull request is submitted, a review is conducted by both the Taxonomy Triage team and the Taxonomy Approvers team to ensure that they are relevant, actionable, and have all of the required information needed to be a valuable addition to the AI model. Triagers might provide feedback and use labels to manage the state of the submitted pull request. Triagers also might provide informative feedback and helpful comments to improve the submission. After the pull request is approved, a Taxonomy Approver merges the skill.

More information regarding basic review questions, subjective review questions, labels, and the reasons for approval, further review requirements, or rejection can be found on the [Triaging Skills](https://github.com/instruct-lab/taxonomy/blob/main/docs/skills-triage.md) page of the GitHub repository.

### How are submissions reviewed?

For code review, the project maintainers use LGTM (Looks Good to Me) in comments on the code review to indicate acceptance. A change requires LGTMs from two of the maintainers.

For skills and knowledge PRs, your PR will be checked to ensure it is relevant, actionable, and has all the information necessary for the approval team to review and merge the PR. The Triage team will use labels to manage the state and action of PRs as well as provide feedback to contributors based upon the following review guidelines:

* Does the PR have the pull request template information filled out?
* Did all the PR checks pass?
* Does the skill have three or more examples?
* Are the YAML fields correct?
* No PII in content
* Does this content include anything documented in the project's [Avoid these Topics](https://github.com/instruct-lab/community/blob/main/docs/README.md#avoid-these-topics) guidelines?
* Does it adhere to the [Code of Conduct](https://github.com/instruct-lab/taxonomy/blob/main/CONTRIBUTING.md#code-of-conduct) guidelines?
* Was a response clearly generated by the LLM?

### How long will it take for my pull request to be reviewed?

Due to the large number of contributions currently being received, it is difficult to provide an exact timeline for reviewing your pull request.

### If my pull request is accepted, how long will it take for my changes to appear in the next model update?

After a pull request is accepted, the changes are regularly incorporated into InstructLab.

### What is the software license for InstructLab?

InstructLab and the Merlinite-7b project are distributed under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

### Am I required to license code submissions to InstructLab under the Apache 2.0 license?

Yes. Code contributions to the InstructLab project are subject to the terms and conditions under the Apache 2.0 license.

### My contribution requires submitting data along with code. What data is permissible to include?

It is recommended that third-party content be licensed with an open data license that does not restrict commercial use or the creation of derivative works, including the following licenses:

* CC0
* CDLA-Permissive
* CC-BY-4.0
* Apache 2.0
* MIT

The InstructLab project follows the same approach (the [Developer's Certificate of Origin 1.1 (DCO)](https://developercertificate.org/)) that [the Linux Kernel community uses](https://docs.kernel.org/process/submitting-patches.html#sign-your-work-the-developer-s-certificate-of-origin) to manage code contributions. Unless the file says otherwise for this project, the relevant open source license is [the Apache License, Version 2.0](https://github.com/instruct-lab/taxonomy/blob/main/LICENSE).  When submitting a patch for review, you must include a sign-off statement in the commit message. See the ["Legal" ](https://github.com/instruct-lab/taxonomy/blob/main/CONTRIBUTING.md#legal) section of the Contributing document.

### Where can I download updated models of InstructLab?

The latest version of InstructLab can be downloaded using the `ilab download` CLI command.

### I have a question about the project. Where should I go?

Currently, the best method for communicating with peers and project maintainers is in the [Community Slack Channel](https://join.slack.com/t/instruct-lab/shared_invite/zt-2ginke0oz-SxvNYZCqBTDy5wzAi9WRlA).

### What are the software and hardware requirements for using InstructLab?

To run InstructLab locally, you must meet the following requirements:

* A Linux-based operating system
* An Apple Silicon M1, M2, or M3 system
* Python 3.9 or later, including the development headers
* Approximately 10GB of free disk space to get through the `ilab generate` step
* Approximately 60GB of free disk space is needed to run the entire process locally on Apple hardware
* About 32 GB RAM

## Additional Resources

Additional resources, including the Code of Conduct, Code of Conduct Committee members, how to contribute, how to join the Slack channel, and more, can be found in the following repositories: 

[InstructLab Taxonomy Repository](https://github.com/instructlab/taxonomy)

[InstructLab CLI Repository](https://github.com/instructlab/cli)

[InstructLab Community Repository](https://github.com/instructlab/community)

Slack and communication

* [Joining the Slack Channel](https://github.com/instructlab/community/blob/main/InstructLabSlackGuide.md)
* [Slack Moderation](https://github.com/instructlab/community/blob/main/InstructLabSlackModerationGuide.md)

