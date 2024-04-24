# Maintainers file generator

Changes to team membership should happen in this way:

* Follow [community
  governance](https://github.com/instructlab/community/blob/main/governance.md)
  practices for [contributor
  roles](https://github.com/instructlab/community/blob/main/CONTRIBUTOR_ROLES.md)
  team membership changes.
* Apply changes to GitHub Team membership via GitHub.
* Run this tool to auto-generate an updated list of team members.

## Requirements

* `pip install -r requirements.txt`
* A working install of the [`gh` command line utility](https://github.com/cli/cli#installation).

## Usage

From the root of the repo:

```
tools/maintainers/maintainers.py tools/maintainers/teams.yaml > MAINTAINERS.md
```
