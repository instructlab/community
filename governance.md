# InstructLab Governance

The following document outlines how the InstructLab project governance operates.

## The InstructLab Project

InstructLab is made up of several projects that are defined as codebases and services with different release cycles. Collectively, these enable large-model development. Currently, these projects include the following:

* [`ilab` command-line interface (CLI) tool](https://github.com/instructlab/instructlab). This repository is responsible for the `ilab` command-line interface (CLI) tool.
* [taxonomy tree](https://github.com/instructlab/taxonomy). This repository is responsible for the taxonomy tree that allows you to create models tuned with your data.

## Governance Structure and Roadmap

The InstructLab Project will evolve into a two-level governance structure with an Oversight Committee and [Project Maintainers](https://github.com/instructlab/community/blob/main/MAINTAINERS.md).

At launch, the InstructLab Project will not have an Oversight Committee to avoid unnecessary overhead. After the majority of project Maintainers agree that the project has grown to the point where an Oversight Committee is necessary, project Maintainers will begin establishment. Until the Oversight Committee is constituted, duties of the Oversight Committee will be assumed by project Maintainers.

Except where otherwise noted, decisions should always start at the most local level of project governance. For example, decisions that affect only one project, such as the taxonomy repository and not the `ilab` CLI tool, can  happen within that project. While communication between the different project teams is important as they are all interconnected, minor decisions do not need organization-wide consensus and can be moved forward at the project level.

Changes in maintainership and other governance are currently announced on the InstructLab community Slack channel. Directions to join the Slack channel can be found [here](https://github.com/instructlab/community/blob/main/InstructLabSlackGuide.md). In the future, a mailing list will be established.

## Project Maintainers overview

Project Maintainers focus on a single codebase, a group of related codebases, a service (for example, a website), or project to support the other projects (such as marketing or community management).

Project Maintainers are responsible for activities surrounding the development and release of code, the operation of any services that they own, or the tasks needed to execute their project (for example, community management or setting up an event booth). Technical decisions for code resides with the project Maintainers unless there is a decision related to cross maintainer groups that cannot be resolved by those groups. Those cases can be escalated to the [organization Maintainers](https://github.com/instructlab/community/blob/main/MAINTAINERS.md).

In some cases, groups of maintainers are responsible for more than one repository, such as `ilab` CLI tool maintainers managing the [taxonomy repository](https://github.com/instructlab/taxonomy).

To be considered an _active project Maintainer_, it is required to be associated with at least one active, non-archived project. If only listed on archived projects, they become _emeritus Maintainers_ and are no longer eligible to become an organization Maintainer.

Project Maintainers do not need to be software developers; however they must be substantial contributors. For example, if a repository is for documentation it would be appropriate for a project Maintainer to be an editor or technical writer.

Advancement to the project Maintainer position, removal or stepping down, and duties are detailed in the [Contributor Roles](https://github.com/instructlab/community/blob/main/CONTRIBUTOR_ROLES.md). The list of current maintainers can be found [here](https://github.com/instructlab/community/blob/main/MAINTAINERS.md).

## InstructLab Oversight Committee overview

The Oversight Committee is selected by project Maintainers and consists of 3 to 9 leaders on the InstructLab project; these members will serve to supervise the overall project and its health. It will also consist of a selected chair member who will set agendas and call meetings; these meetings can be public or private at the discretion of the Oversight Committee.

The Oversight Committee is responsible for the following duties:

* Maintaining the mission, vision, values, and scope of the project
* Refining the governance and charter as needed
* Making project level decisions, including setting technical policies that apply across all components
* Resolving escalated project decisions when the team responsible is blocked
* Managing the InstructLab brand
* Controlling access to InstructLab assets such as source repositories and hosting
* Appointing members to the [Code of Conduct Committee](https://github.com/instructlab/community/blob/main/COCC.md)
* Deciding what projects are part of the InstructLab project
* Overseeing the resolution and disclosure of security issues
* Managing financial decisions related to the project

Until the Oversight Committee is selected, these duties will be carried out by the project Maintainers.

### InstructLab Cross-Component Technical Policies

Cross-component technical policies are out of scope for this project governance document, but can be found in the [InstructLab Enhancements Repo](https://github.com/instructlab/enhancements/blob/main/README.md).

### Oversight Committee selection process

The Oversight Committee will be selected and maintained using the following process:

A project Maintainer of any active (non-archived) InstructLab organization project is eligible for a position as an organization Maintainer. Once a year, the Oversight Committee will be re-elected. The election will consist of a nomination period followed by an election period. Any person who has made a contribution to any repository under the [InstructLab GitHub](https://github.com/instructlab) organization may nominate a suitable project Maintainer of an active project.

The election will proceed according to the following process:

1. The nomination period will be three weeks. This period starts from the day after an organization Maintainer opening becomes available.

1. The nomination must be made on the InstructLab community Slack channel. Directions to join the Slack channel can be found [here](https://github.com/instructlab/community/blob/main/InstructLabSlackGuide.md). In the future, a mailing list will be established for nominations.

1. After a nominated individual(s) agrees to be a candidate for the Oversight Committee, project Maintainers will vote. The voting period will be open for a minimum of three business days. It will remain open until a [supermajority](https://en.wikipedia.org/wiki/Supermajority#Two-thirds_vote) of project Maintainers has voted. Only current Maintainers of active projects are eligible to vote.

1. When the number of nominated individuals matches the number of openings, each individual must have a _Yes_ vote from a supermajority of those that voted.

1. When there are more individuals than open positions, voting will use a _Ranked Choice_ voting method, such as [Condorcet](https://en.wikipedia.org/wiki/Condorcet_method).

### Resignation or Departure from the Maintainer or the Oversight Committee role

Project Maintainers or Oversight Committee members may resign or could be expelled as follows:

* Maintainers or an Oversight Committee member may step down through email. Within 7 calendar days, organization contributors and Maintainers will be notified on the InstructLab community Slack channel. Directions to join the Slack channel can be found [here](https://github.com/instructlab/community/blob/main/InstructLabSlackGuide.md). In the future, a mailing list will be established.

* After an Oversight Committee member steps down, they become an emeritus Maintainer.

* Maintainers and Committee members MUST remain active on the project. In the event that an Oversight Committee member or a Maintainer is unresponsive or inactive for more than 3 months, they may be removed by a supermajority vote.

* Maintainers and Oversight Committee members who have violated the [Code of Conduct](https://github.com/instructlab/community/blob/main/CODE_OF_CONDUCT.md) may be removed by a supermajority vote of the remaining Oversight Committee members.

## Decision making at the InstructLab organization level

Generally, there are methods for decision making for the InstructLab project: by lazy consensus or by voting.

The default decision making process is [_lazy-consensus_](http://communitymgt.wikia.com/wiki/Lazy_consensus). This means that any decision is considered supported by the team making it so long as no one objects. Silence on any consensus decision is implicit agreement, and equivalent to explicit agreement. Explicit agreement may be stated at will.

When a consensus cannot be met, a Maintainer can call for a [majority](https://en.wikipedia.org/wiki/Majority) vote on a decision.

Many of the day-to-day project maintenance can be done by through the lazy consensus model.

The secondary decision making process is done by voting. The following items must be called to a vote and conducted by the appropriate body:

* Appointing or removing a member of the [Code of Conduct Committee](https://github.com/instructlab/community/blob/main/COCC.md) (supermajority)
* Carrying out [Code of Conduct](https://github.com/instructlab/community/blob/main/CODE_OF_CONDUCT.md) decisions requiring severe censure (majority)
* Removing a [Maintainer](https://github.com/instructlab/community/blob/main/MAINTAINERS.md) for any reason other than inactivity (supermajority)
* Changing the governance (that is, this document's) rules (supermajority)
* Licensing and intellectual property changes such as new logos or wordmarks (simple majority)
* Adding, archiving, or removing projects (simple majority)

Other decisions may, but do not need to be, called out and put up for decision  on the InstructLab community Slack channel. Directions to join the Slack channel can be found [here](https://github.com/instructlab/community/blob/main/InstructLabSlackGuide.md). In the future, a mailing list will be established. This can be done by anyone at any time. By default, any decisions called to a vote will be for a _simple majority_ vote.

## Code of Conduct

InstructLab's [Code of Conduct](https://github.com/instructlab/community/blob/main/CODE_OF_CONDUCT.md) is enforced by the [Code of Conduct Committee (CoCC)](https://github.com/instructlab/community/blob/main/COCC.md). This committee will be appointed and removed by the Oversight Committee, or by the project Maintainers before the Oversight Committee is created, using a supermajority vote.  

The CoCC is responsible for investigating, evaluating, and recommending remedies for substantiated Code of Conduct incidents to the appropriate body. The CoCC will judge possible violations around principles of restorative justice rather than punishment. All teams within InstructLab are obligated to support the CoCC's recommendations on remedies.

Current CoCC members can be found on the [Code of Conduct Committee](https://github.com/instructlab/community/blob/main/COCC.md) page.

Possible Code of Conduct violations should be reported to the Code of Conduct Committee on the InstructLab community Slack channel. Directions to join the Slack channel can be found [here](https://github.com/instructlab/community/blob/main/InstructLabSlackGuide.md). In the future, a mailing list will be established.

## Developer Certificate of Origin (DCO) and Licenses

The following licenses and contributor agreements will be used for InstructLab projects:

* [Apache 2.0](https://opensource.org/licenses/Apache-2.0) for code
* [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode) for documentation
* [Developer Certificate of Origin](https://developercertificate.org/) for new contributions

## Modifications to this Governance

This governance may be modified by a supermajority of the Oversight Committee, or by a supermajority of all project Maintainers.
