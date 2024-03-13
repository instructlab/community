# InstructLab Governance

The following document outlines how the InstructLab project governance operates.

## The InstructLab Project

The InstructLab project is made up of several Projects, defined as codebases and services with different release cycles, that enable large model development. These Projects currently include:

* cli - a tool to chat and train models
* taxonomy - tree that enables model creation tuned with your data

The services provided include:

* Documentation for those who want to chat, and train models
* Public taxonomy collaboration

## Governance Structure and Roadmap

The InstructLab Project will evolve into a two-level governance structure with an Oversight Committee and Project Maintainers.  In order to avoid unnecessary overhead, at launch the project will not have a Oversight Committee. Once the majority of Project Maintainers feel that the project has grown to the point where an Oversight Committee is necessary, the Maintainers will vote to select one. Until the Oversight Committee is constituted, the duties of the Committee will be assumed by the collective Project Maintainers.

Except where otherwise noted, decisions should always start at the most local level of project governance.  For example, decisions that affect only one Project should happen within that Project. Only escalate in the the event of problems.

Changes in maintainership and other governance are announced on the **TODO: InstructLab mailing list**.

### InstructLab Oversight Committee

The InstructLab Oversight Committee (OC) will consist of 3 to 9 of the leaders of the InstructLab project who have been chosen to serve on a team to supervise the general project and its health. The Oversight Committee are selected by the project Maintainers.

The Oversight Committee are responsible for:

* Maintaining the mission, vision, values, and scope of the project
* Refining the governance and charter as needed
* Making project level decisions
* Resolving escalated project decisions when the team responsible is blocked
* Managing the InstructLab brand
* Controlling access to InstructLab assets such as source repositories, hosting, project calendars
* Appointing the Code of Conduct Committee
* Deciding what projects are part of the InstructLab project
* Overseeing the resolution and disclosure of security issues
* Managing financial decisions related to the project

Until the Oversight Committee is selected, the duties above will be carried out by the collective project Maintainers.

Once instantiated, the Oversight Committee will be selected and maintained using the following process:

Any Maintainer of any active (non-archived) InstructLab organization project is eligible for a position as an org maintainer.  Once a year, the Oversight Committee will be re-elected.  The election will consist of a nomination period followed by an election period.  Any person who has made a contribution to any repo under the InstructLab GitHub org may nominate a suitable Project Maintainer of an active project.

The election will proceed according to the following process:
* The nomination period will be three weeks starting the day after an org maintainer opening becomes available
* The nomination must be made via the **TODO: InstructLab mailing list**
* When nominated individual(s) agrees to be a candidate for maintainership, the project maintainers may vote
* The voting period will be open for a minimum of three business days and will remain open until a super-majority of project maintainers has voted
* Only current project maintainers of active projects are eligible to vote
* When the number of nominated individuals matches the number of openings each individual needs to have a yes vote from a super-majority of those that voted
* When there are more individuals than open positions voting will use a Ranked Choice voting mehtos, such as [Condorcet](https://en.wikipedia.org/wiki/Condorcet_method)

Aside from the elections, the Oversight Committee members may leave the committee as follows:

* A member may step down by emailing the Oversight Committee mailing list. Within 7 calendar days the **TODO: InstructLab mailing list** will be notified of the change
* Committee members MUST remain active on the project. If they are unexpectedly unresponsive for more than 3 months, or are otherwise not fulfilling their duties, or have violated the Code of Conduct, they may be removed by a vote of a [super-majority](https://en.wikipedia.org/wiki/Supermajority#Two-thirds_vote) of the remaining OC members
* After an OC member steps down, they become an emeritus maintainer

The Oversight Committee will select a chair to set agendas and call meetings.  Some meetings of the Oversight Committee will be public, and others will be private, at the OC's discretion.

### Project Maintainers

Project Maintainers focus on a single codebase, a group of related codebases, a service (e.g., a website), or project to support the other projects (e.g., marketing or community management).

Project maintainers are responsible for activities surrounding the development and release of code, the operation of any services they own (e.g., the documentation site), or the tasks needed to execute their project (e.g., community management, setting up an event booth). Technical decisions for code resides with the project maintainers unless there is a decision related to cross maintainer groups that cannot be resolved by those groups. Those cases can be escalated to the org maintainers.

In some cases a groups of maintainers are responsible for more than one repo (e.g., cli maintainers managing taxonomy). In other cases the maintainers are responsible for a single project (e.g., cli).

To be considered active maintainers, it is required for maintainers to be associated with at least one active, non-archived project. If only listed on archived projects, they become emeritus project maintainers and are no longer eligible to become org maintainers.

Project maintainers do not need to be software developers, but they do need to be substantial contributors.  For example, if a repository is for documentation it would be appropriate for maintainers to be editors.

Advancement to Project Maintainer position, removal, and duties are detailed in the [Contributor Ladder](/CONTRIBUTOR_LADDER.md).  The [current maintainers](/MAINTAINERS.md) are listed in this repository.

## Decision Making at the InstructLab org level

When maintainers need to make decisions there are two ways decisions are made, unless described elsewhere.

The default decision making process is [lazy-consensus](http://communitymgt.wikia.com/wiki/Lazy_consensus). This means that any decision is considered supported by the team making it as long as no one objects. Silence on any consensus decision is implicit agreement and equivalent to explicit agreement. Explicit agreement may be stated at will.

When a consensus cannot be found a maintainer can call for a [majority](https://en.wikipedia.org/wiki/Majority) vote on a decision.

Many of the day-to-day project maintenance can be done by a lazy consensus model. But the following items must be called to vote of the appropriate body:

* Appointing or removing a member of the Code of Conduct Committee (super majority)
* Carrying out Code of Conduct decisions requiring severe censure (majority)
* Removing a maintainer for any reason other than inactivity (super majority)
* Changing the governance rules (this document) (super majority)
* Licensing and intellectual property changes (including new logos, wordmarks) (simple majority)
* Adding, archiving, or removing projects (simple majority)

Other decisions may, but do not need to be, called out and put up for decision on the **TODO: InstructLab mailing list** at any time and by anyone. By default, any decisions called to a vote will be for a _simple majority_ vote.

## Code of Conduct

InstructLab's [Code of Conduct] is enforced by the Code of Conduct Committee (CoCC).  This committee will be appointed and removed by the Oversight Committee, or by the Project Maintainers before the OC is created, using a supermajority vote.  

The CoCC is responsible for investigating, evaluating, and recommending remedies for substantiated Code of Conduct Incidents to the appropriate body. The CoCC will judge possible violations around principles of restorative justice rather than punishment. All teams within InstructLab are obligated to support the CoCC's recommendations on remedies.

These are the current members of the [Code of Conduct Committee](/CoCC.md).

Possible code of conduct violations should be emailed to the CoCC at **TODO: Private CoC mailing list**.

## DCO and Licenses

The following licenses and contributor agreements will be used for InstructLab projects:

* [Apache 2.0](https://opensource.org/licenses/Apache-2.0) for code
* [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode) for documentation
* [Developer Certificate of Origin](https://developercertificate.org/) for new contributions

## Modifications to this Governance

This governance may be modified by a super-majority of the Oversight Committee, or by a super-majority of all Project Maintainers.
