# Maintainers file generator

Changes to team membership should happen in this way:

* Follow [community
  governance](../../GOVERNANCE.md)
  practices for [contributor
  roles](../../CONTRIBUTOR_ROLES.md)
  team membership changes.
* Apply changes to GitHub Team membership via GitHub.
* Run this tool to auto-generate an updated list of team members.

## Requirements

* `pip install -r requirements.txt`
* A working install of the [`gh` command line utility](https://github.com/cli/cli#installation).

## Usage

From the root of the repo:

```shell
tools/maintainers/maintainers.py tools/maintainers/teams.yaml > MAINTAINERS.md
```
