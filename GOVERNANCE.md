# InstructLab Governance

The following document outlines how the InstructLab project governance operates.

## The InstructLab Project

InstructLab is made up of several projects that are defined as codebases and services with different release cycles. Collectively, these enable large-model development. Currently, these projects include the following:

* [`ilab` command-line interface (CLI) tool](https://github.com/instructlab/instructlab). This repository is responsible for the `ilab` command-line interface (CLI) tool.
* [taxonomy tree](https://github.com/instructlab/taxonomy). This repository is responsible for the taxonomy tree that allows you to create models tuned with your data.

## Governance Structure and Roadmap

The InstructLab Project has a two-level governance structure with an Oversight Committee and [Project Maintainers](https://github.com/instructlab/community/blob/main/MAINTAINERS.md).

Except where otherwise noted, decisions should always start at the most local level of project governance. For example, decisions that affect only one project, such as the taxonomy repository and not the `ilab` CLI tool, can happen within the taxonomy project. While communication between the different project teams is important as they are all interconnected, minor decisions do not need organization-wide consensus and can be moved forward at the project level.

Changes in maintainership and other governance are currently announced on the InstructLab community Slack channel. Directions to join the Slack channel can be found [here](https://github.com/instructlab/community/blob/main/InstructLabSlackGuide.md). Changes are also announced to the [announce mailing list](https://github.com/instructlab/community/blob/main/Collaboration.md#email-lists).

## Project Maintainers overview

Project Maintainers focus on a single codebase, a group of related codebases, a service (for example, a website), or a project to support other projects (such as marketing or community management).

Project Maintainers are responsible for activities surrounding the development and release of code, the operation of any services that they own, or the tasks needed to execute their project (for example, community management or setting up an event booth). Technical decisions for code reside with the project Maintainers unless there is a decision related to multiple maintainer groups that cannot be resolved by those groups. Those cases can be escalated to the Oversight Committee.

To be considered an _active project Maintainer_, it is required to be associated with at least one active, non-archived project. If only listed on archived projects, they become _emeritus Maintainers_ and are no longer eligible to become an organization Maintainer.

Project Maintainers do not need to be software developers; however, they must be substantial contributors. For example, if a repository is for documentation it would be appropriate for a project Maintainer to be an editor or technical writer.

Advancement to the project Maintainer position, removal or stepping down, and duties are detailed in the [Contributor Roles](https://github.com/instructlab/community/blob/main/CONTRIBUTOR_ROLES.md). The list of current maintainers can be found [here](https://github.com/instructlab/community/blob/main/MAINTAINERS.md).

## InstructLab Oversight Committee Overview

The initial Oversight Committee at the launch of the project was appointed by the founding sponsors of the InstructLab project. This bootstrap committee will serve until the first election of the Oversight Committee using processes and timing as determined by this group.

The list of Oversight Committee members can be found [here](https://github.com/instructlab/community/blob/main/MAINTAINERS.md#oversight-committee).

The Oversight Committee consists of 3 to 7 leaders on the InstructLab project.  These members will serve to supervise the overall project and its health. It will also consist of a selected Chair member who will set agendas and call meetings. These meetings can be public or private at the discretion of the Oversight Committee.

The Oversight Committee is responsible for the following duties:

* Maintaining the mission, vision, values, and scope of the project
* Refining the governance and charter as needed
* Making project-level decisions, including setting technical policies that apply across all components
* Resolving escalated project decisions when the team responsible is blocked
* Managing the InstructLab brand
* Controlling access to InstructLab assets such as source repositories and hosting
* Appointing members to the [Code of Conduct Committee][committee]
* Deciding what projects are part of the InstructLab project
* Overseeing the resolution and disclosure of security issues
* Managing financial decisions related to the project

### Draft Oversight Committee selection process

> [!NOTE]
> This section is a draft. It is a responsibility of the initial Oversight
> Committee to finalize this process.

The Oversight Committee will be selected and maintained using the following process:

A project Maintainer of any active (non-archived) InstructLab organization project is eligible for a position as an organization Maintainer. Once a year, the Oversight Committee will be re-elected. The election will consist of a nomination period followed by an election period. Any person who has made a contribution to any repository under the [InstructLab GitHub](https://github.com/instructlab) organization may nominate a suitable project Maintainer of an active project.

The election will proceed according to the following process:

1. The nomination period will be three weeks. This period starts from the day after an organization Maintainer opening becomes available.

1. The nomination must be made on the InstructLab [community mailing list](https://github.com/instructlab/community/blob/main/Collaboration.md#email-lists).

1. After a nominated individual agrees to be a candidate for the Oversight Committee, project Maintainers will vote. The voting period will be open for a minimum of three business days. It will remain open until a [supermajority](https://en.wikipedia.org/wiki/Supermajority#Two-thirds_vote) of project Maintainers have voted. Only current Maintainers of active projects are eligible to vote.

1. When the number of nominated individuals matches the number of openings, each individual must have a _Yes_ vote from a supermajority of those who voted.

1. When there are more individuals than open positions, voting will use a _Ranked Choice_ voting method, such as [Condorcet](https://en.wikipedia.org/wiki/Condorcet_method).

### Resignation or Departure from the Maintainer or the Oversight Committee role

Project Maintainers or Oversight Committee members may resign or could be expelled as follows:

* Maintainers or an Oversight Committee member may step down through email. Within 7 calendar days, organization contributors and Maintainers will be notified on the InstructLab [community mailing list](https://github.com/instructlab/community/blob/main/Collaboration.md#email-lists).

* After an Oversight Committee member steps down, they become an emeritus Maintainer.

* Maintainers and Committee members MUST remain active on the project. In the event that an Oversight Committee member or a Maintainer is unresponsive or inactive for more than 3 months, they may be removed by a supermajority vote.

* Maintainers and Oversight Committee members who have violated the [Code of Conduct](https://github.com/instructlab/community/blob/main/CODE_OF_CONDUCT.md) may be removed by a supermajority vote of the remaining Oversight Committee members.

## Decision making at the InstructLab organization level

Generally, there are methods for decision making for the InstructLab project: by lazy consensus or by voting.

The default decision-making process is [_lazy-consensus_](http://communitymgt.wikia.com/wiki/Lazy_consensus). This means that any decision is considered supported by the team making it so long as no one objects. Silence on any consensus decision is implicit agreement, and equivalent to explicit agreement. An explicit agreement may be stated at will.

When a consensus cannot be met, a Maintainer can call for a [majority](https://en.wikipedia.org/wiki/Majority) vote on a decision.

Many of the day-to-day project maintenance can be done through the lazy consensus model.

The secondary decision-making process is done by voting. The following items are examples that must be called to a vote and conducted by the appropriate body:

* Appointing or removing a member of the [Code of Conduct Committee][committee] (supermajority of the Oversight Committee)
* Carrying out [Code of Conduct](https://github.com/instructlab/community/blob/main/CODE_OF_CONDUCT.md) decisions requiring severe censure (majority of the Code of Conduct committee)
* Removing a [Maintainer](https://github.com/instructlab/community/blob/main/MAINTAINERS.md) for any reason other than inactivity (supermajority of the Oversight Committee)
* Non-trivial changes to the governance (this document) (supermajority of the Oversight Committee)
* Licensing and intellectual property changes such as new logos or wordmarks (majority of the Oversight Committee)
* Adding, archiving, or removing projects (majority of the Oversight Committee)

Other decisions may be called out and put up for decision on the InstructLab [community mailing list](https://github.com/instructlab/community/blob/main/Collaboration.md#email-lists). This can be done by anyone at any time. By default, any decisions called to a vote will be for a _simple majority_ vote of the Oversight Committee.

## Code of Conduct

InstructLab's [Code of Conduct](https://github.com/instructlab/community/blob/main/CODE_OF_CONDUCT.md) is enforced by the [Code of Conduct Committee (CoCC)][committee]. This committee will be appointed and removed by the Oversight Committee using a supermajority vote.

The CoCC is responsible for investigating, evaluating, and recommending remedies for substantiated Code of Conduct incidents to the appropriate body. The CoCC will judge possible violations around principles of restorative justice rather than punishment. All teams within InstructLab are obligated to support the CoCC's recommendations on remedies.

Current CoCC members can be found on the [Code of Conduct Committee][committee] page.

Possible Code of Conduct violations should be reported to the Code of Conduct Committee via the [Code of Conduct email alias](https://github.com/instructlab/community/blob/main/Collaboration.md#email-lists).

## Developer Certificate of Origin (DCO) and Licenses

The following licenses and contributor agreements will be used for InstructLab projects:

* [Apache 2.0](https://opensource.org/licenses/Apache-2.0) for code
* [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode) for documentation
* [Developer Certificate of Origin](https://developercertificate.org/) for new contributions

## Modifications to this Governance

This governance may be modified by a supermajority vote of the Oversight Committee.

Trivial changes that do not introduce policy changes may be approved by two members of the Oversight Committee.

[committee]: https://github.com/instructlab/community/blob/main/CODE_OF_CONDUCT_COMMITTEE.md
