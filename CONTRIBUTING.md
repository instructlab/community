# Contributing

👍🎉 First off, thank you for taking the time to contribute! 🎉👍

The following is a set of guidelines for contributing. These are just guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## What to know before getting started

### Code of Conduct

This project adheres to a [Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

Please report unacceptable behavior to one of the Code of Conduct [Committee members](./COCC).

### Related repositories

In addition to this repository, InstructLab has two related repositories:

* [`ilab` command-line interface (CLI) tool](https://github.com/instruct-lab/cli). This repository is responsible for the `ilab` command-line interface (CLI) tool.
* [taxonomoy tree](https://github.com/instruct-lab/taxonomy). This repository is responsible for the taxonomy tree that allows you to create models tuned with your data.

The following sections provide a general overview for contributing to any of the InstructLab repositories.

## Contributing overview

Participating in the InstructLab project can come by contributing to any one of the repositories. The following workflow is designed to help you understand contribution best practices, and to help you begin your contribution journey. It will guide you through creating and picking up issues, working through them, having your work reviewed, and then getting your pull request merged.

Help on open source projects is always welcome and there is always something that can be improved. For example, documentation (like the text you are reading now) can always use improvement, code can always be clarified, variables or functions can always be renamed or commented on, and there is always a need for more test coverage. If you see something that you think should be fixed, take ownership!

To contribute code or documentation, please submit a pull request to the relevant repository. Note that contribution to any repository has its own set of requirements and expectations, and users should familiar themselves with those expectations before contributing.

### ilab command-line interface (CLI) tool repository

We welcome contributions in the form of pull requests for documentation updates, code contributions and more. Prior to contribution, users should acquaint themselves with the [`ilab` CLI repository contribution guide](https://github.com/instruct-lab/cli/blob/main/CONTRIBUTING/CONTRIBUTING.md).

To submit a pull request to the `ilab` CLI tool repository, see the [pull request page](https://github.com/instruct-lab/cli/pulls).

### Taxonomy repository

We welcome contributions in the form of pull requests for documentation updates, skills contributions, knowledge contributions and more. Prior to contribution, users should acquaint themselves with the [taxonomy repository contribution guide](https://github.com/instruct-lab/taxonomy/blob/main/CONTRIBUTING.md).

To submit a pull request to the taxonomy repository, see the [pull request page](https://github.com/instruct-lab/taxonomy/pulls).

### Community

We welcome contributions in the form of pull requests for documentation. To submit a pull request to the community repository, see the [pull request page](https://github.com/instruct-lab/community/pulls).

### Getting started with contribution

The InstructLab project uses the _Fork and Pull_ model for contribution that is common in many open source repositories; this entails multiple steps, including forking and cloning the repository, creating a _pull request_, or PR, and more. For details on this process, check out [The GitHub Workflow
Guide](https://github.com/kubernetes/community/blob/master/contributors/guide/github-workflow.md) from Kubernetes. If you are already familiar with this process, the taxonomy repository provides [detailed contribution instructions](https://github.com/instruct-lab/taxonomy/blob/main/README.md#detailed-contribution-instructions) as an example.

After you have forked and cloned the repository, you can start the contribution process by looking at the issue trackers of the [community repository](https://github.com/instruct-lab/community/pulls), [CLI repository](https://github.com/instruct-lab/cli/issues), or the [taxonomy repository](https://github.com/instruct-lab/taxonomy/issues). You can then pick up an issue by leaving a comment on said issue, and address the issue in a pull request (PR). Prior to submission, make sure that your changes pass formatting, linting, and unit tests. Additionally, all PRs must agree to the terms of [Developer Certificate of Origin (DCO)](https://developercertificate.org/) by signing off your commits. Only PRs with commits signed off are accepted. If you didn't sign off your commits before creating the pull request, no worries, you can fix that after the fact. For more information about this process, see [Developer Certificate of Origin (DCO)](#DCO).

Then, you can submit the PR to be reviewed. In general, we follow the standard [GitHub pull request](https://help.github.com/en/articles/about-pull-requests) process. Follow the provided template on your PR to include details about your pull request for the maintainers.

> **IMPORTANT:** If you are seeking to make a larger contribution, such as introducing a new feature or functionality, or refactoring a significant portion of the codebase to improve performance, readability, or maintainability, [get in touch](#communication) with us prior to starting. This helps ensure that your time is not wasted working on a change that the project developers will not accept into the codebase.

### Pull request review

Once you've created a pull request (PR), maintainers will review your code and may make suggestions to fix before merging. It will be easier for your PR to receive reviews if you consider the criteria the reviewers follow while working. Remember to:

- Run tests locally and ensure that they pass
- Follow the project coding conventions
- Write detailed commit messages
- Break large changes into a logical series of smaller patches, which are easy to understand individually and combine to solve a broader issue

The project maintainers use `LGTM` (Looks Good To Me) in comments on the code review to indicate acceptance. A change requires LGTMs from two of the
maintainers of each component affected.

For a list of the maintainers and triagers, see the [MAINTAINERS.md](MAINTAINERS.md) page.

### Proposing new features

To propose a new feature, it's best to raise an issue in the appropriate repository:

- [CLI repository](https://github.com/instruct-lab/cli/issues)
- [taxonomy repository](https://github.com/instruct-lab/taxonomy/issues)

This way, features can be discussed with the project maintainers, ensuring that your time is not wasted working on a feature that the project developers will not accept into the codebase.

### Submitting or fixing bugs

To submit a new bug, raise an issue in the appropriate repository before creating a pull request. This ensures that the issue is appropriately tracked.

To fix an existing bug, leave a comment on the issue that you are working on. Then, create a pull request and submit the pull request for review.

## Legal

The following sections detail important legal information that should be viewed prior to contribution.

### License and Copyright

Distributed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

SPDX-License-Identifier: [Apache-2.0](https://spdx.org/licenses/Apache-2.0)

If you would like to see the detailed LICENSE click [here](LICENSE).

### Developer Certificate of Origin (DCO)

We have tried to make it as easy as possible to make contributions. This applies to how we handle the legal aspects of contribution. We use the same approach - the [Developer's Certificate of Origin 1.1 (DCO)](https://developercertificate.org/) - that the Linux® Kernel [community](https://docs.kernel.org/process/submitting-patches.html#sign-your-work-the-developer-s-certificate-of-origin)
uses to manage code contributions.

We ask that when submitting a patch for review, the developer must include a sign-off statement in the commit message. If you set your `user.name` and `user.email` in your `git config` file, you can sign your commit automatically by using the following command:

```shell
git commit -s
```

The following example includes a `Signed-off-by:` line, which indicates that the submitter has accepted the DCO:

```
Signed-off-by: John Doe <john.doe@example.com>
```

We automatically verify that all commit messages contain a `Signed-off-by:` line with your email address.

#### Useful tools for doing DCO signoffs <DCO id="DCO resources"></DCO>

There are a number of tools that make it easier for developers to manage DCO signoffs.

- DCO command line tool, which let's you do a single signoff for an entire repo ( <https://github.com/coderanger/dco> )
- GitHub UI integrations for adding the signoff automatically ( <https://github.com/scottrigby/dco-gh-ui> )
- Chrome - <https://chrome.google.com/webstore/detail/dco-github-ui/onhgmjhnaeipfgacbglaphlmllkpoijo>
- Firefox - <https://addons.mozilla.org/en-US/firefox/addon/scott-rigby/?src=search>

## Communication

You can use the dedicated [Discussion Board](https://github.com/orgs/instruct-lab/discussions) for the InstructLab project to communicate with project maintainers.

## Additional resources

The following resources include additional information about each repository, such as setting up the environment, testing the environment, coding styles, etc.

### ilab CLI tool additional resources

- [`ilab` CLI tool README.md](https://github.com/instruct-lab/cli/blob/main/README.md#instructlab--ilab). This resources provides information about the `ilab` CLI tool, including an overview, getting started, training the model, submitting a pull request, etc.

- [`ilab` CLI tool CONTRIBUTING.md](https://github.com/instruct-lab/cli/blob/main/CONTRIBUTING/CONTRIBUTING.md#contributing). This resources provides information about contributing to the `ilab` CLI tool repository, reporting bugs, testing, coding styles, etc.

### Taxonomy additional resources

- [Taxonomy README.md](https://github.com/instruct-lab/taxonomy/blob/main/README.md). This resource provides information about the taxonomy repository, including getting started, YAML examples for skills and knowledge pull requests, how to contribute, etc.

- [Taxonomy CONTRIBUTING.md](https://github.com/instruct-lab/taxonomy/blob/main/CONTRIBUTING.md). This resource contains information and best practices for contributing to the taxonomy repository.