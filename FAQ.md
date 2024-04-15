# InstructLab FAQ

Last updated: April 2024

## Document summary

This page serves as a comprehensive FAQ for the InstructLab project, detailing how it works, how to contribute, and the goals behind the project. Key information includes:

* **InstructLab Overview**: This open-source project allows users to interact with and train the Merlinite-7b AI Large Language Model (LLM) by contributing skills and knowledge.
* **LAB Method**: A synthetic data-based tuning method for LLMs consisting of a taxonomy-driven data curation process, a synthetic data generator, and two-phased training with replay buffers.
* **Contribution Process**: Contributors can add skills or knowledge to the LLM by creating YAML files and testing changes locally before submitting a pull request to InstructLab’s GitHub repository.
* **Project Goals**: To democratize contributions to AI and LLMs, allowing rapid model development through community collaboration facilitated by nightly builds integrating community contributions.

For more specific questions about the InstructLab CLI and troubleshooting common issues, see [General lab CLI tool FAQs](https://github.com/instruct-lab/cli/discussions/648).

For more specific questions about the taxonomy repository, see [Taxonomy repository FAQ](https://github.com/instruct-lab/taxonomy/discussions/538).

## General FAQ

### What is InstructLab?

InstructLab (**L**arge-scale **A**lignment for chat**B**ots) is an open-source initiative by Red Hat and IBM. It provides a platform for easy engagement with the Merlinite -7b AI Large Language Model (LLM) by using the `ilab` command-line interface (CLI) tool. You can use the CLI to work with Merlinite-7b to test new skills and knowledge, for example, asking it to tell a joke or answer a question about a particular subject. Users can then augment the LLM’s capabilities by submitting the skills and knowledge they have tested to the project’s taxonomy repository on GitHub by creating a pull request. This approach encourages community-driven enhancements without the need for complex model forking or fine-tuning of the model, promoting rapid development through collaborative contributions.

### What is LAB?

LAB (**L**arge-scale **A**lignment for chat**B**ots) is a novel synthetic data-based align tuning method for LLMs from IBM Research. It consists of three components:


1. A taxonomy-drive data curation process
2. A large-scale synthetic data generator
3. Two-phased-training with replay buffers

The LAB approach allows incrementally adding new knowledge and skills to an already pre-trained model without catastrophic forgetting.

More information about the LAB method can be found on the [Hugging Face project page](https://huggingface.co/ibm/merlinite-7b).

### How does InstructLab work?

InstructLab is driven by taxonomies, or _trees of skills_, and works by empowering users to add new _skills_ and _knowledge_ to a pre-trained LLM.

Contributors to InstructLab first [download](https://github.com/instruct-lab/cli?tab=readme-ov-file#-getting-started) the `ilab` CLI, which allows them to chat with a pre-trained LLM. If a contributor finds that a specific knowledge domain of the LLM is lacking, they can add a [new skill or knowledge](https://github.com/instruct-lab/taxonomy?tab=readme-ov-file#getting-started-with-skill-contributions) (or build upon existing skills/knowledge) to the model and test it locally. This is done by creating a simple YAML file that includes information about the topic they seek to improve. After adding the YAML file to their local taxonomy repository, they can run the `ilab generate` command and generate new synthetic training data based on the changes of the local taxonomy repository, which re-trains the LLM with new information. Users can then chat with the re-trained LLM to see the results.

After testing the LLM locally to confirm the information is accurate, contributors can improve the AI model by[ submitting a pull request to InstructLab’s taxonomy repository on GitHub](https://github.com/instruct-lab/taxonomy?tab=readme-ov-file#detailed-contribution-instructions). This requires users to fork the taxonomy repository, create a pull request, and get the content of the pull request approved and merged by a repository administrator. After the pull request is merged, the AI model is upgraded during a nightly build. Contributors can then update their local deployment by running the `ilab download` command to obtain the latest model.

### What are the goals of the InstructLab project?

In its current state, openly contributing to a large language model (LLM) has been difficult because of the large compute infrastructure needed to run one.

The InstructLab project seeks to democratize the contribution to AI and LLMs through its _taxonomy_, or _tree of skills_, repository. When users contribute to the InstructLab project, the taxonomy repository resynthesizes the open-source training data for InstructLab-trained LLMs. The model is then re-trained regularly (nightly builds), ensuring that community contributions are integrated while enriching the model’s capabilities over time.

### Why should I contribute?

InstructLab is designed to enable collaboration around Merlinite-7b, an open-source LLM that contributors can access through [Hugging Face](https://huggingface.co/ibm/merlinite-7b). Participating is an opportunity to contribute to open-source AI regardless of technical background.

When contributors write an extension to the existing taxonomy, make a pull request, and get it reviewed and merged, their changes are rolled out in the next nightly build. This update strategy expedites the model’s capabilities and allows contributors to see the impact that they have made on the model much sooner than other LLMs.

### What large language models (LLMs) am I contributing to through the InstructLab project?

Contributions to the InstructLab project update Merlinite-7b, an open-source LLM. Contributors have direct access to the model they are improving through [Hugging Face](https://huggingface.co/ibm/merlinite-7b).

### What is Merlinite-7b?

Merlinite-7b is a Mistral-7b derivative model trained with the LAB (**L**arge-scale **A**lignment for chat**B**ots) using Mixtral-8x7b-Instruct as a teacher model.

More information about the Merlinite-7b can be found on the [Hugging Face project page](https://huggingface.co/ibm/merlinite-7b).

### What is a “skill”?

In the context of InstructLab, a _skill_ is a capability or knowledge domain submitted by a contributor intending to train the AI model on the submitted information. In other words, when you submit a skill, you teach the AI model _how to do something_.

InstructLab skills are broken down into two main categories:

* **Foundational skills.** Foundational skills are skills like math, reasoning, and coding.
* **Composition skills.** Composition or _performative_ skills allow AI models to perform specific tasks or functions. With InstructLab, there are two types of composition skills:
    * **Freeform compositional skills** are performative skills that do not require additional context. For example, to train an AI model to tell cat jokes, you would provide examples of cat jokes.
    * **Grounded compositional skills** are performative skills that require additional context. One example is how an AI model reads the value of a cell in a table layout. To create the grounded skill to read a table formatted in Markdown, the additional context might be an example table layout.

Skills are written in a YAML file and submitted to the InstructLab upstream project for review. The following pull requests can  serve as models for your own skills submission:

* Freeform skill: [Introducing Gen Z phrases](https://github.com/instruct-lab/taxonomy/pull/79)
* Grounded skill: [Finding unresolved items in a meeting transcript](https://github.com/instruct-lab/taxonomy/pull/250)

### What is “knowledge”?

Knowledge consists of data and facts. When creating knowledge for an AI model, you are providing it with additional data and information to answer questions more accurately. Whereas skills are the information that trains an AI model on how to do something, knowledge is based on the AI model’s ability to answer questions that involve facts, data, or references.

Like skills, knowledge submissions are submitted in YAML format to the InstructLab upstream project for review. The following pull requests can  serve as models for your own skills submission:

* [Add QnA about music theory](https://github.com/instruct-lab/taxonomy/pull/230)
* [Add information about the 7 wonders of the world](https://github.com/instruct-lab/taxonomy/pull/50)

### What are the requirements for submitting a skill or knowledge?

To submit a skill or knowledge contribution, you must have a GitHub account and access to the InstructLab taxonomy repository.

While there are no strict guidelines for skills submissions, they should seek to address gaps in the knowledge domains of the LLM. Generally speaking, recognizing a knowledge gap comes from using and testing the model locally. After you have identified a gap in a specific skill or knowledge, you can contribute in one of two ways:

* You can make a public contribution directly to the [taxonomy repository](https://github.com/instruct-lab/taxonomy).
* You can [fork](https://github.com/instruct-lab/taxonomy?tab=readme-ov-file#detailed-contribution-instructions) this repository under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

For more information about forking the repository, see [Detailed Contribution Instructions](https://github.com/instruct-lab/taxonomy?tab=readme-ov-file#detailed-contribution-instructions).

### Is the project looking for certain types of skill contributions?

Currently, InstructLab only accepts compositional (_freeform_ and _grounded_) skills and knowledge. However, any type of freeform or grounded skill can be submitted. Some skills might not be added to the taxonomy repository for reasons such as duplication, submitting a skill that the model already does well, or submitting a controversial skill.

Foundational skills are not currently being accepted.

### What are the acceptance criteria for a skills submission?

Skills should seek to add capabilities or a knowledge domain to the AI model; in other words, a skills submission should teach the AI model _how to do something_ instead of providing information _about something_. A good skills submission might address something that the AI model does poorly and seek to enhance its ability to execute that capability better. For example, if you find that the AI model does not execute telling jokes well, you might add skills to improve them.

Skills submissions that are unlikely to be accepted include submitting a knowledge request instead of a skills request, submitting a skill that the model already does well, submitting a controversial skill, or submitting skills that do not execute pure math or coding.

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
* Does it adhere to the [code of conduct](https://github.com/instruct-lab/taxonomy/blob/main/CONTRIBUTING.md#code-of-conduct) guidelines?
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

The InstructLab project follows the same approach (the [Developer's Certificate of Origin 1.1 (DCO)](https://developercertificate.org/)) that [the Linux Kernel community uses](https://docs.kernel.org/process/submitting-patches.html#sign-your-work-the-developer-s-certificate-of-origin) to manage code contributions. Unless the file says otherwise for this project, the relevant open source license is [the Apache License, Version 2.0](https://github.com/instruct-lab/taxonomy/blob/main/LICENSE).  When submitting a patch for review, you must include a sign-off statement in the commit message. See the [“legal” ](https://github.com/instruct-lab/taxonomy/blob/main/CONTRIBUTING.md#legal)section of the “[Contributing.md](https://github.com/instruct-lab/taxonomy/blob/main/CONTRIBUTING.md)” document.

### Where can I download updated models of InstructLab?

The latest version of InstructLab can be downloaded using the `ilab download` CLI command.

### What are the software and hardware requirements for using InstructLab?

To run InstructLab locally, you must meet the following requirements:

* A Linux-based operating system
* An Apple Silicon M1, M2, or M3 system
* Python 3.9 or later, including the development headers
* Approximately 10GB of free disk space to get through the `ilab generate` step.
* Approximately 60GB of free disk space is needed to run the entire process locally on Apple hardware.

## Additional Resources

[InstructLab Taxonomy Repository](https://github.com/instruct-lab/taxonomy)

* [ReadMe](https://github.com/instruct-lab/taxonomy/blob/main/README.md)
* [Contributing](https://github.com/instruct-lab/taxonomy/blob/main/CONTRIBUTING.md)
* [License](https://github.com/instruct-lab/taxonomy/blob/main/LICENSE)
* [Code of Conduct](https://github.com/instruct-lab/taxonomy/blob/main/CODE_OF_CONDUCT.md)
* [Taxonomy repository FAQ](https://github.com/instruct-lab/taxonomy/discussions/538)

[InstructLab CLI Repository](https://github.com/instruct-lab/cli)

* [ReadMe](https://github.com/instruct-lab/cli/blob/main/README.md)
* [Contributing](https://github.com/instruct-lab/cli/blob/main/CONTRIBUTING/CONTRIBUTING.md)
* [License](https://github.com/instruct-lab/cli/blob/main/LICENSE)
* [Code of Conduct](https://github.com/instruct-lab/cli/blob/main/CODE_OF_CONDUCT.md)
* [General lab CLI tool FAQs](https://github.com/instruct-lab/cli/discussions/648)
* [Discussion board](https://github.com/instruct-lab/cli/discussions)

[InstructLab Community Repository](https://github.com/instruct-lab/community)

* Getting started
