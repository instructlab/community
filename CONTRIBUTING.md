# Contributing

👍🎉 First off, thank you for taking the time to contribute! 🎉👍

The following is a set of guidelines for contributing. These are just guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## What to know before getting started

### Code of Conduct

This project adheres to a [Code of Conduct](./CODE_OF_CONDUCT.md) adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html. By participating, you are expected to uphold this code.

[homepage]: https://www.contributor-covenant.org.


Please report unacceptable behavior to one of the [Code Owners](./CODEOWNERS).

## Contributing in general

The below workflow is designed to help you begin your first contribution journey. It will guide you through creating and picking up issues, working through them, having your work reviewed, and then merging.

Help on open source projects is always welcome and there is always something that can be improved. For example, documentation (like the text you are reading now) can always use improvement, code can always be clarified, variables or functions can always be renamed or commented on, and there is always a need for more test coverage. If you see something that you think should be fixed, take ownership!

To contribute code or documentation, please submit a [pull request](/pulls) in the relevant repository.

> **IMPORTANT:** For all PRs, you need to agree to the terms of [Developer Certificate of Origin (DCO)](https://developercertificate.org/) by signing off your commits. We automatically verify that all commit messages contain a `Signed-off-by`: line with your email address.

You can include a signoff automatically when you commit a change to your local git repository using the following command:

```shell
git commit -s
```
We can only accept PRs that have all commits signed off. If you didn't sign off your commits before creating the pull request, no worries, you can fix that after the fact. For more information, see [Useful tools for doing DCO signoffs](#DCO).

### How to get started

When contributing, it's useful to start by looking at[issue tracker](/issues) of the repository you would like to contribute to. After picking up an issue, writing code, or updating a document, make a pull request and your work will be reviewed and merged.

To contribute, you'll use the Fork and Pull model common in many open source repositories. For details on this process, check out [The GitHub Workflow
Guide](https://github.com/kubernetes/community/blob/master/contributors/guide/github-workflow.md)
from Kubernetes.

When your contribution is ready, you can create a pull request. Pull requests are often referred to as "PR". In general, we follow the standard [GitHub pull request](https://help.github.com/en/articles/about-pull-requests) process. Follow the template to provide details about your pull request to the maintainers.

Before sending pull requests, make sure your changes pass formatting, linting and unit tests.
Before embarking on an ambitious contribution, please quickly [get in touch](#communication) with us.


### Proposing new features
If you're adding a new feature or find a bug, it's best to [raise an issue](/issues)
in the appropriate respository before sending a pull request so that the feature can be
discussed with the maintainers. Discussion helps us avoid wasting your valuable time working on a feature that the project developers are not interested in accepting into the code base.

### Fixing bugs

If you would like to fix a bug, please [raise an issue](/issues) in the appropriate repository
before sending a pull request so it can be tracked.

### Code review

Once you've [created a pull request](#how-can-i-contribute), maintainers will review your code and may make suggestions to fix before merging. It will be easier for your pull request to receive reviews if you consider the criteria the reviewers follow while working. Remember to:

- Run tests locally and ensure they pass
- Follow the project coding conventions
- Write detailed commit messages
- Break large changes into a logical series of smaller patches, which are easy to understand individually and combine to solve a broader issue

The project maintainers use LGTM (Looks Good To Me) in comments on the code review to indicate acceptance. A change requires LGTMs from two of the
maintainers of each component affected.

For a list of the maintainers and triagers, see the [MAINTAINERS.md](MAINTAINERS.md) page.

## Ways to contribute to InstructLab

### Taxonomy

We welcome contributions in the form of pull requests for documentation updates, skills contributions, knowledge contributions and more.

>**NOTE:** knowledge contributions will not be considered at launch but will be accepted at a later date.
See the [Taxonomy's contribution guide](https://github.com/instruct-lab/taxonomy/blob/main/CONTRIBUTING.md) for more details.

### CLI

We welcome contributions in the form of pull requests for documentation updates, code contributions and more.
See the [CLI's contribution guide](https://github.com/instruct-lab/cli/blob/main/CONTRIBUTING/CONTRIBUTING.md) for more details.

## Legal

### License and Copyright

Each source file must include a license header for the Apache
Software License 2.0. Using the SPDX format is the simplest approach.
e.g.

```
/*
Copyright <holder> All Rights Reserved.

SPDX-License-Identifier: Apache-2.0
*/
```
### DCO

We have tried to make it as easy as possible to make contributions. This applies to how we handle the legal aspects of contribution. We use the same approach - the [Developer's Certificate of Origin 1.1 (DCO)](https://developercertificate.org/) - that the Linux® Kernel [community](https://docs.kernel.org/process/submitting-patches.html#sign-your-work-the-developer-s-certificate-of-origin)
uses to manage code contributions.

We ask that when submitting a patch for review, the developer must include a sign-off statement in the commit message.

Here is an example Signed-off-by line, which indicates that the submitter accepts the DCO:

```
Signed-off-by: John Doe <john.doe@example.com>
```

If you set your `user.name` and `user.email` in your `git config` file, you can sign your
commit automatically with `git commit -s` command.

### Useful tools for doing DCO signoffs <DCO id="DCO resources"></DCO>

There are a number of tools that make it much easier for developers to manage DCO signoffs.

- DCO command line tool, which let's you do a single signoff for an entire repo ( <https://github.com/coderanger/dco> )
- GitHub UI integrations for adding the signoff automatically ( <https://github.com/scottrigby/dco-gh-ui> )
- Chrome - <https://chrome.google.com/webstore/detail/dco-github-ui/onhgmjhnaeipfgacbglaphlmllkpoijo>
- Firefox - <https://addons.mozilla.org/en-US/firefox/addon/scott-rigby/?src=search>

## Communication

Please use our [Discussion Board](https://github.com/orgs/instruct-lab/discussions) to communicate with the maintainers.

## Setup

Please see each repo's README.md or CONTRIBUTING.md files for any testing guidelines and requirements.

## Testing

Please see each repo's README.md or CONTRIBUTING.md files for any testing guidelines and requirements.

## Coding style guidelines

Please see each repo's CONTRIBUTING.md file for any coding style guidelines and requirements.



