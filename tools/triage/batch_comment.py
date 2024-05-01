from github import Github
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Comment on a bunch of PRs....")
    parser.add_argument('-t', '--token', type=str, help="GitHub PAT to authenticate against")
    parser.add_argument('-prs', nargs="+", type=int, help="The list of PRs you want to comment on", required=True)
    parser.add_argument('-pc', '--precheck', help="Send the precheck comment", action="store_true")
    parser.add_argument('-gen', '--generate', help="Send the generate comment", action="store_true")
    args = parser.parse_args()

    list_of_prs = list(args.prs)

    if args.precheck:
        comment = '@instructlab-bot precheck'
    if args.generate:
        comment = '@instructlab-bot generate'

    if args.token:
        GITHUB_TOKEN = args.token
    else:
        GITHUB_TOKEN = os.environ.get("GH_TOKEN")

    if GITHUB_TOKEN is None:
        print("You need a token to talk to GitHub, use 'GH_TOKEN' as an ENV var, or -t in the command")
        exit(1)

    for i in list_of_prs:
        g = Github(GITHUB_TOKEN)
        repo_name = os.environ.get("REPO_NAME", "instructlab/taxonomy")
        repo = g.get_repo(repo_name)
        pr = repo.get_issue(i)
        print(f"Commenting on {i} now....")
        pr.create_comment(comment)


if __name__ == "__main__":
    exit(main())
