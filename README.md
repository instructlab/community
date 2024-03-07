<!-- This should be the location of the title of the repository, normally the short name -->
# InstructLab Community 
There is a great need for rapid innovation on open models.
There's AI in the open and then there's open source AI. 

![image](https://github.com/instruct-lab/community/assets/85503753/25fcefc7-a7ac-4511-90df-dc397ba741d5)

## Why InstructLab
AI becomes stronger, more stable and secure with an open approach to large model development.There are many projects rapidly embracing and extending permissively licensed AI models, but they are faced with three main challenges:
* Contribution to the models themselves is not possible directly.  They show up as forks, which forces consumers to choose a “best-fit” model that isn’t easily extensible, and the forks are expensive for model creators to maintain.
* The ability to contribute ideas is limited by a lack of AI/ML expertise.  One has to learn how to fork, train, and refine models in order to see their idea move forward.  This is a very high barrier to entry.
* There is no direct community governance or best practice around review, curation, and distribution of forked models.

## Technical Overview
InstructLab is an automated instruction-based model tuning method and toolset that accelerates and standardized model knowledge and skill composition and alignment to instruction following. It utilizes a model content and prompt behavior configuration standard to specify, and then generate and refine synthetic training data and deploy it through a novel training method. This process enables adding user-specified knowledge and skills (a “model pull request”) to various open model baselines, and merge various pull requests (model “merge”) into a single model. It also results in standardized and predictable prompting behavior even as the model content and alignment changes, Tests today have demonstrated rapid cycles of progress with small teams (~few developers) updating various open models with new skills and higher accuracy benchmarking (e.g. MT Bench). 


## Goals
This open-source community effort must accomplish, at least, the following goals:
* Build out, validate, and drive adoption of the InstructLab tooling and model API standard.
* Grow ecosystem of open data (inputs) and open models (outputs) as enablers and proof points.
* Establish deployable app patterns, practices and proof points for sophisticated use cases.


## Usage

* [LICENSE](LICENSE)
* [README.md](README.md)
* [CONTRIBUTING.md](CONTRIBUTING.md)
* [MAINTAINERS.md](MAINTAINERS.md)
<!-- A Changelog allows you to track major changes and things that happen, https://github.com/github-changelog-generator/github-changelog-generator can help automate the process -->
* [CHANGELOG.md](CHANGELOG.md)


## Legal & Governance
- [InstructLab Community Governance](Need to create)
- [InstructLab Code of Conduct](https://github.com/instruct-lab/community/tree/main?tab=coc-ov-file)


## Resources
- [InstructLab Website]()
- [InstructLab Mailing lists]()



<!-- Questions can be useful but optional, this gives you a place to say, "This is how to contact this project maintainers or create PRs -->
If you have any questions or issues you can create a new [issue here](https://github.com/instruct-lab/community/issues).

Pull requests are very welcome! Make sure your patches are well tested.
Ideally create a topic branch for every separate change you make. For
example:

1. Fork the repo
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## License

All source files must include a Copyright and License header. The SPDX license header is 
preferred because it can be easily scanned.

If you would like to see the detailed LICENSE click [here](LICENSE).

```text
#
# Copyright IBM Corp. {Year project was created} - {Current Year}
# SPDX-License-Identifier: Apache-2.0
#
```

