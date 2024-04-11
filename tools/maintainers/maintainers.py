#!/usr/bin/env python

import json
import subprocess
import sys

import yaml


def get_team_members(team_slug):
    org = 'instruct-lab'
    result = subprocess.run(['gh', 'api', '--method', 'GET',
                             f'/orgs/{org}/teams/{team_slug}/members'],
                             stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    return json.loads(output)


def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) != 2:
        print("Usage: maintainers.py <path-to-teams-yaml>")
        return 1

    teams_yaml = argv[1]

    with open(teams_yaml, 'r') as f:
        teams = yaml.load(f, Loader=yaml.FullLoader)
        print("# Maintainers\n")
        for section, teams in teams.items():
            print("## %s\n" % section)
            for t in teams:
                print("### %s\n" % t["name"])
                members = get_team_members(t["slug"])
                for m in members:
                    print("- [%s](https://github.com/%s)" % (m["login"], m["login"]))
                print("\n")

    return 0


if __name__ == '__main__':
    sys.exit(main())