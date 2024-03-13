# Contributor Ladder for InstructLab

This document outlines a default number of contributor roles for InstructLab projects. Promotion within the roles is based on individual participation using transparent criteria. These criteria should be re-evaluated periodically to ensure we can meet the needs of the projects with the resources available to contribute. Also, these criteria can be extended by an individual project to meet the project's specific needs.

| Role       | Responsibilities                             | Requirements                                                  | Defined by                    |
|------------|----------------------------------------------|---------------------------------------------------------------|-------------------------------|
| Member     | Active contributor in the community          | Multiple contributions and sponsored by 2 maintainers            | InstructLab GitHub org member        |
| Triager    | Triaging issues and PRs                      | History of issue and PR triage and sponsored by 2 maintainers           | InstructLab GitHub Triage team member        |
| Reviewer   | Reviews contributions from other contributors     | History of reviews and contributions. Sponsored by 2 maintainers.                             | CODEOWNERS/MAINTAINER file reviewer entry  |
| Maintainer | Set direction and priorities for the project | Demonstrated responsibility and excellent technical judgement. Nominated and approved by maintainers team. | CODEOWNERS/MAINTAINER file approver entry  |

The project welcomes new contributors. Not all contributors are able to provide sustained contribution, but each contribution is always welcome.  Established contributors are expected to demonstrate their adherence to the criteria in this document, familiarity with project organization, roles, policies, etc., and technical and/or writing ability. Role-specific expectations, responsibilities, and requirements are enumerated below.

## Member

Members are active contributors in the community. They can have issues and PRs assigned to them. Members are expected to remain active contributors to the community.

**Defined by:** Member of the InstructLab GitHub organization.

### Requirements

- Have made multiple contributions to the project or community. Contribution may include, but is not limited to:
    - Authoring or reviewing PRs on GitHub.
    - Filing or commenting on issues on GitHub.
    - Contributing to community discussions (e.g. meetings, Slack).
- Sponsored by two maintainers.

If you meet the requirements, nominate yourself as below,
- Open an issue in the repo of interest.
- Ensure your sponsors are @mentioned on the issue.
- Make sure that the list of contributions included is representative of your work on the project.

### Responsibilities and Privileges

- Responsive to issues and PRs assigned to them.
- Active owner of code they have contributed (unless ownership is explicitly transferred):
    - Provide well tested code that consistently pass tests.
    - Addresses bugs or issues discovered after code is accepted.

**Note:** Members who frequently contribute code are expected to proactively
perform code reviews and work towards becoming a *reviewer* for the project they are active in.

## Triager

Triagers are active contributors in the community through issue and PR triage. Triagers are expected to remain active in this task.

**Defined by:** Member of the InstructLab GitHub Triage team.

### Requirements

- Have made multiple contributions to the project or community. Contribution may include, but is not limited to:
    - Triaging open issues or PRs.
    - Authoring or reviewing PRs on GitHub.
    - Contributing to community discussions (e.g. meetings, Slack).
- Sponsored by two maintainers.

If you meet the requirements, nominate yourself as below,
- Open an issue in the repo of interest.
- Ensure your sponsors are @mentioned on the issue.
- Make sure that the list of contributions included is representative of your work on the project.

### Responsibilities and Privileges

- Have permission to label issues and PRs.
- Assign, close, and reopen issues or PRs.
- Expected to actively triage issues and PRs with high quality.

## Reviewer

Reviewers are the members with high quality code contributions and who have demonstrated greater skill in reviewing the code. They are knowledgeable about both the codebase and software engineering principles. Their LGTM counts towards merging a code change by maintainers.

**Defined by:** *reviewers* entry in the CODEOWNERS/MAINTAINER file.

### Requirements

- Member for at least 1 month.
- Primary reviewer for at least 5 PRs to the codebase with high quality reviews.
- Knowledgeable about the codebase.
- Sponsored by two maintainers.

If you meet the requirements, nominate yourself to become a reviewer by sending an email to maintainers with your candidacy.
- Ensure your sponsors are @mentioned on the email.
- Include a list of contributions representative of your work on the project.
- Existing maintainers will vote privately and respond to the email with either acceptance or with feedback for suggested improvement.
- Upon all maintainers agreement or lazy consensus among them in a three week time frame, a maintainer will create PR to add you in the CODEOWNERS/MAINTAINER file.

### Responsibilities and Privileges

- Responsible for project quality control via code reviews.
- Focus on code quality and correctness, including testing and factoring.
- Expected to be responsive to review requests.
- Assigned PRs to review related to area of expertise.
- Assigned test bugs related to area of expertise.
- Unless otherwise specified review LGTMs are considered as one of the LGTMs required for merge of a commit for a project.

## Maintainer

Maintainers are first and foremost contributors that have shown they are committed to the long term success of a project. Maintainership is about building trust with the current maintainers and being a person that they can depend on to make decisions in the best interest of the project in a consistent manner.

**Defined by:** *approvers* entry in the CODEOWNERS/MAINTAINER file.

### Requirements

- Reviewer for at least 1 month.
- Deep understanding of the technical goals and direction of the project.
- Deep understanding of the technical domain of the project.
- Sustained contributions to design and direction by doing all of:
    - Authoring and reviewing proposals.
    - Initiating, contributing and resolving discussions (emails, Slack, GitHub issues, meetings).
    - Identifying subtle or complex issues in designs and implementation PRs.
- Directly contributed to the project through implementation and / or review.

If you meet the requirements, nominate yourself to become a maintainer by sending an email to maintainers with your candidacy.
- Ensure your sponsors are @mentioned on the email.
- Include a list of contributions representative of your work on the project.
- Existing maintainers will vote privately and respond to the email with either acceptance or with feedback for suggested improvement.
- Upon all maintainers agreement or lazy consensus among them in three week time frame, a maintainer will nominate you publicly and create PR to add you in the CODEOWNERS/MAINTAINER file.

### Responsibilities and Privileges

- Make and approve technical design decisions.
- Set technical direction and priorities.
- Define milestones and releases.
- Mentor and guide reviewers, and contributors to the project.
- Ensure continued health of the project.
- Adequate test coverage to confidently release.
- Tests are passing reliably (i.e. not flaky) and are fixed when they fail.
- Ensure a healthy process for discussion and decision making is in place.
- Work with other maintainers to maintain the project's overall health and success holistically.
- Unless otherwise specified, maintainers of a project are the github users with permission to merge commits to the project repository branches.

### Stepping Down/Emeritus Process

Life priorities, interests, and passions can change. Maintainers can retire and move to emeritus maintainers. If a maintainer needs to step down, they should inform other maintainers, if possible, help find someone to pick up the related work. At the very least, ensure the related work can be continued. Afterward they can remove themselves from the list of existing maintainers.

If a maintainer has not been performing their duties for a consecutive period of 12 months, they can be removed by the other maintainers from the active maintainer list. In that case the inactive maintainer will be first notified via an email. If the situation doesn't improve, they will be moved from the active list to an emeritus list. If an emeritus maintainer wants to regain an active role, they can do so by renewing their contributions. Active maintainers should welcome such a move. Retiring of other maintainers or regaining the status should require approval of at least two active maintainers.

## Acknowledgements

Contributor roles and responsibilities were written based on various CNCF projects membership and [Contributor Ladder Template](https://github.com/cncf/project-template/blob/main/CONTRIBUTOR_LADDER.md).
