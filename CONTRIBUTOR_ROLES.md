# Contributor roles for InstructLab

InstructLab is made up of several projects that are defined as codebases and services with different release cycles. Collectively, these enable large-model development. Currently, these projects include the following:

* [`ilab` command-line interface (CLI) tool](https://github.com/instructlab/instructlab). This repository is responsible for the the `ilab` CLI tool.
* [taxonomy tree](https://github.com/instructlab/taxonomy). This repository is responsible for the taxonomy tree that allows you to create models tuned with your data.

This document outlines a core number of contributor roles for InstructLab projects, such as _Member_, _Triager_, and _Maintainer_. An _Oversight Committee_ also serves to supervise the overall InstructLab project and its health. Using transparent criteria, the journey between roles is based on individual participation.

Criteria will be reevaluated periodically to ensure that we can meet the needs of each project with the resources available to contribute. Each individual project may add to or change these criteria as necessary. Additional roles may also be added as required. Additional roles will be detailed in a _Contributor Roles_ file in the respective repository when necessary. If no _Contributor Roles_ file exists in a repository, it is assumed to follow the scheme outlined here.

Contributor roles are per-project. For example, being a Maintainer for the `ilab` CLI repository does not guarantee that you will have Maintainer rights for the taxonomy repository. Where applicable for InstructLab overall, contributor status is equal to the highest status that they have on any project.

InstructLab welcomes new contributors. Not all contributors are able to provide sustained contribution, but each contribution is welcome. Established contributors are expected to demonstrate their adherence to the criteria in this document, familiarity with project organization, roles, policies, etc., and technical and/or writing ability. Role-specific expectations, responsibilities, and requirements are explained below.

## Current roles

The following table provides information about the current roles available to the InstructLab project.

| Role       | Responsibilities                             | Requirements                                                  | Defined by                    |
|------------|----------------------------------------------|---------------------------------------------------------------|-------------------------------|
| Member     | Active contributor in the community          | Multiple contributions and sponsored by 2 Maintainers         | InstructLab GitHub org member |
| Triager    | Triaging issues and PRs                      | History of issue and PR triage and sponsored by 2 Maintainers           | InstructLab GitHub Triage team member        |
| Maintainer | Sets direction and priorities for a project | Demonstrated responsibility and excellent technical judgement. Nominated and approved by Maintainers team. | [MAINTAINERS file](https://github.com/instructlab/community/blob/main/MAINTAINERS.md) Maintainer entry  |

### Member

Members are active contributors in the community. They can have issues and pull requests (PRs) assigned to them. Members are expected to be active contributors to the community.

**Defined by:** Member of the InstructLab GitHub organization.

#### Member requirements

To become a project Member, you must meet the following requirements:

* You have made multiple contributions to the project or community. Contributions may include, but are not limited to:

  * Authoring or reviewing PRs on GitHub.
  * Filing or commenting on issues on GitHub.
  * Contributing to community discussion, for example, meetings or on Slack.

* You have been sponsored by two Maintainers.

If you have met these expectations and wish to become an established member, you can be nominated by a contributor, or you can nominate yourself. To nominate a contributor or yourself:

* Open an issue in the repository of interest detailing contributions to the project so far.
* Ensure that the sponsors are `@mentioned` on the issue.
* Make sure that the list of contributions included is representative of the work on the project.

#### Member responsibilities and privileges

As a project Member, you have the following responsibilities and privileges:

* You are responsive to issues and the pull requests assigned to them.
* You are an active owner of code that you have contributed, unless ownership is explicitly transferred:
  * You provide code that consistently pass tests.
  * You consistently address bugs or issues that are discovered after code has been accepted.

### Triager

Triagers are active contributors in the community through issue and pull request triage. Triagers are expected to remain active in this task.

**Defined by:** Member of the InstructLab GitHub Triage team.

#### Triager requirements

To become a project Triager, you must meet the following requirements:

* You have made multiple contributions to the project or community. Contribution may include, but is not limited to:
  * Triaging open issues or PRs.
  * Authoring or reviewing PRs on GitHub.
  * Contributing to community discussions (e.g. meetings, Slack).

* You have been sponsored by two Maintainers.

Any person who meets the requirements may be nominated by a contributor, including themselves. To nominate a contributor or yourself:

* Open an issue in the repository of interest detailing contributions to the project so far.
* Ensure that the sponsors are `@mentioned` on the issue.
* Make sure that the list of contributions included is representative of the work on the project.

#### Triager responsibilities and privileges

As a project Triager, you have the following responsibilities and privileges:

* You have permission to label issues and PRs.
* You consistently assign, close, and reopen issues or PRs.
* You actively triage issues and PRs with high quality.

### Maintainer

Maintainers are first and foremost contributors that have shown they are committed to the long term success of a project. Maintainership is about building trust with the community and being a person that everyone can depend on to make consistent decisions in the best interest of the project.

**Defined by:** _Maintainers_ entry in the [MAINTAINER file](https://github.com/instructlab/community/blob/main/MAINTAINERS.md).

#### Maintainer requirements

To become a project Maintainer, you must meet the following requirements:

* You have been a Member for at least 1 month.
* You have a deep understanding of the technical goals and direction of the project.
* You have a deep understanding of the technical domain of the project.
* You have made sustained contributions to design and direction by:
  * Authoring and reviewing proposals.
  * Initiating, contributing, and resolving discussions, such as emails, Slack, GitHub issues, meetings.
  * Identifying subtle or complex issues in designs and implementation pull requests.
* You have directly contributed to the project through implementation and/or review.
* You have been sponsored by two Maintainers.

One of the sponsors should open an issue in the relevant repository to provide a nomination. The issue should use the provided nomination template if one exists in that repo. If one does not exist, the sponsor should create a template prior to creating the nomination.

Maintainers will vote publicly on the issue, expressing their support via a GitHub comment or emoji reaction to the nomination summary. Any concerns may be discussed privately amongst the existing Maintainer team. If feedback needs to be given to the nominee, the sponsor should provide that feedback privately.

After a [decision has been made](https://github.com/instructlab/community/blob/main/governance.md#decision-making-at-the-instructlab-org-level), a Maintainer will create a PR to add you in the [MAINTAINER file](https://github.com/instructlab/community/blob/main/MAINTAINERS.md) within three weeks.

#### Maintainer responsibilities and Privileges

As a project Maintainer, you have the following responsibilities and privileges:

* You make and approve technical design decisions.
* You set technical direction and priorities.
* You define milestones and releases.
* You mentor and guide contributors to the project, including mentoring and sponsoring potential Triager and Maintainer candidates.
* You ensure the continued health of the project.
* You are responsive to review requests.
* You review assigned PRs that are related to your area of expertise.
* You focus on quality and correctness, including testing code and factoring content.
* You are responsible for project quality control via code reviews.
* You perform adequate test coverage to confidently release.
* The tests that you perform are passing reliably (i.e. not flaky) and are fixed when they fail.
* You ensure that a healthy process for discussion and decision making is in place.
* You work with other Maintainers to maintain the project's overall health and success holistically.
* Unless otherwise specified, you will be provided with permission to merge commits to the project repository branches.

## Stepping Down and the Emeritus Process

Life priorities, interests, and passions can change. Contributors can retire and move to _emeritus Maintainers_. If a contributor needs to step down from their current role, they should inform the appropriate project Maintainers.  No vote is required for a contributor to remove themselves, and any project Maintainer can approve the PR. Maintainers who step down become emeritus Maintainers.

If a contributor has not been performing the duties of their role for a consecutive period of 12 months, they can be removed by the appropriate project's Maintainers. Maintainers will make reasonable efforts to contact the absent contributor. If the [Code of Conduct Committee][committee] recommends that a contributor be removed from their role, this will also be carried out by the project Maintainers.  

If an emeritus Maintainer or other retired contributor wants to regain an active role, they can do so by renewing their contributions, after which they can be re-instated by a decision of the appropriate project's Maintainers.

## Changes by Oversight Committee Members

The Oversight Committee has authority over all team membership. A member of the
Oversight Committee may make changes to team membership, including adding or
removing members, at their discretion. When such changes are made, the Oversight
Committee member should notify the rest of the Oversight Committee so they are
aware of the changes.

## Changes to contributor roles

Changes to contributor roles must be approved by a vote of the Oversight Committee or a majority of the current project's Maintainers.

## Acknowledgements

Contributor roles and responsibilities were written based on various CNCF projects membership and the [Contributor Ladder Template](https://github.com/cncf/project-template/blob/main/CONTRIBUTOR_LADDER.md).

[committee]: https://github.com/instructlab/community/blob/main/CODE_OF_CONDUCT_COMMITTEE.md
