## Triage

Triage is useful to ensure no submission fails to get attention. It also

- speeds up issue management;
- keeps contributors engaged by shortening response times;
- prevents work from lingering endlessly;
- replaces special requests and one-offs with a neutral process that acts like a boundary;
- provides greater transparency, interesting discussions, and more collaborative, informed decision-making;
- builds prioritization, negotiation and decision-making skills, which are critical to most tech roles; and
- reinforces community and culture.

### Labels

Each repository should have a set of labels to use for triaging purposes.

Usual labels include the following options in this table.

Label | Use
--|--
`do-not-merge` or `hold` | Indicates the pull request needs to wait for some reason
`duplicate` | Indicates the issue or PR is a duplicate of different work (usually the later issues/PRs are the ones flagged as duplicate)
`kind-bug` | Indicates a bug that can be picked up
`kind-support` | Indicates the issue is a question for how-to or troubleshooting help
`needs-information` | Indicates the triager needs information from the contributor
`triage-needed` | Indicates the issue or PR has not yet been touched (usually automatic)

## Responding to contributions

Keep these ideas in mind:
- When responding to any contributor in issues, pull requests, or a forum, remember that you are temporarily the public representative of the InstructLab project. **Be welcoming and friendly.** If you don't have an answer, always add someone else who might know in the comment in the reply.
- **Respond within one week to any open contributions**, and use the triage labels to indicate what your response was. For Slack or Discord, use threads to respond to questions or comments as much as possible.
- **Know when and how to say no.** Sometimes requests or contributions need to be declined, at least in their current form. Find and follow any guidelines in each repository to understand common issues or edge cases. Don't be afraid to link to them in your reply. Be polite, but firm in your response. It saves everyone's time and patience to make expectations clear early.
  - However, also hold your strong opinions loosely. If a community member provides a rationale for a change, be willing to listen and discuss with fellow triagers and maintainers.
- **Always first say thank you for the contribution**, even if it cannot be accepted. No matter how big or small, the person contributing the work put time in. Whether it's a bug report, a spelling fix in documentation, or a new feature, all contributions are valuable (even issues that turn out not to be a bug; it's an opportunity to fix the docs!).

### Example issue and PR responses

These responses were written with the understanding that sometimes there will be a need to have internal discussions that cannot go onto GitHub. **In general, it’s better to discuss inside the issue or PR with the contributor if possible so there is continued activity and the contributor does not feel ignored.** Here are some initial responses you can use and customize to get more comfortable answering contributors in a repo you want to monitor.

Start with this snippet:

> Thanks for the <feedback/commits/bug report>!

If you respond, provide an answer, code review, or information why we’re rejecting the PR (e.g., “We already went through this path back in <#>, and we decided that it would be better to avoid it because of X, Y, and Z. Thanks for the idea, though!”). If the author has more work to do on a PR to meet the standards from the repo like generating missing tests or linting the project, here’s a good starting point:

> We really appreciate your contribution! Before we can merge this in, however, we need to ensure that this PR meets our contribution guidelines found in <link>. Namely, this PR <is missing tests/needs to be linted with this command/etc.>. Do you need help getting that part squared away?

You may need to offer to help them with any workflows in Git or the command line, such as amending commits for signoff.

If you can’t answer, add this snippet:

>I don’t have a great answer for you, but I am going to take this back to our team and have someone get back to you within <timeframe> so we can work together to figure out the next steps.

The key is that timeframe at the end. Ensure the timeframe is something you can make happen, even if it’s another reply that says you’re still working on getting the information, like this:

> Just a quick note. I’m still tracking down an answer for you. We haven’t forgotten about you!

Ensure you always follow up until the contributor gets an answer. It’s best to follow up once a week. Two weeks gets a bit long for a community member to wait, and often they feel like they’ve been forgotten. If that happens too many times, they stop coming to the community for assistance or stop contributing to a project because they feel like they don’t have a say.

If the PR/issue hasn’t had a response for a while, add to the starting snippet a simple “Sorry for the delay.” with no further excuse or explanation. Don't spend a ton of time apologizing; long apologies can sound hollow and may cause a community member to respond in frustration.

### Example forum responses

Start with this snippet:

> Thanks for posting! That’s a great question/insight.

If you can answer, provide an answer.

If you can’t answer, add this snippet:

> I don’t have a great answer for you, but I am going to take this back to the rest of the maintainers and have someone get back to you within <timeframe>.

The key is that timeframe at the end. Ensure the timeframe is something you can make happen, even if it’s another reply that says you’re still working on getting the information, like this:

>Just a quick note. I’m still tracking down an answer for you. We haven’t forgotten about you!

Ensure you always follow up until the contributor gets an answer. Generally in an async place like a forum, it’s best to follow up once a week. Two weeks gets a bit long for a community member to wait, and often they feel like they’ve been forgotten. If that happens too many times, they stop coming to the community for assistance.

### Handling difficult or contentious situations

Even experienced professionals need time to respond in a way to diffuse the situation, and sometimes you may need to go for a walk or talk with someone else to get some breathing room before crafting a response. That's normal; please find a peer maintainer or triager if you need a sounding board.

Always attempt to de-escalate a situation through calm, neutral responses.

---

These guidelines have been adapted from the following sources:
- The TLDR maintainer's guide ([CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)): https://github.com/tldr-pages/tldr/blob/main/contributing-guides/maintainers-guide.md
- The Kubernetes project triage guides([Apache 2.0](https://github.com/kubernetes/community/blob/master/LICENSE)): https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md
- Personal experience (@nimbinatus)