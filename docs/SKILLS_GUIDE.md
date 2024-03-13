# Skills Guide

## What is a "Skill"?

### Core Skills

    Core skills are foundational skills like math, reasoning, and coding.

    🗒️ **Note:** Unlike **knowledge** and **compositional skills**, core skills
    are not contributable to the tree. So when you see reference to contributing
    "skills" to the taxonomy from this point forward, it is **compositional
    skills** that are being referenced.
### Compositional Skills

    Skills are performative. When you create a skill for the model, you're
    teaching it how to do something: "write me a song," "talk like a pirate," or
    "summarize an email."

There are two types of compositional skills:

#### Freeform Compositional Skills

     Freeform compositional skills are performative and do **not** require
     additional context. An example of a compositional skill is "talk like a
     pirate." You could provide examples of "pirate-like" speech. By providing
     those examples, you're essentially tickling the latent knowledge of the
     LLM. In our "talk like a pirate" example, you're enabling the LLM to be
     able to recall pirate-like speeches in its latent knowledge.

    Freeform skills include things like:
      * Speak like Yoda
      * Jokes about chickens
      * Convert to camel case
      * Write me a limerick
      * Generate StabeDiffusion prompts
      * ASCII art creation
      
#### Grounded Compositional Skills

    [Example PR](https://github.com/instruct-lab/taxonomy/pull/250)

     Grounded skills are performative and **do** require additional context. An
     example of a grounded skill would be to read the value of a cell in a table
     layout, or to parse a JSON file. To create a grounded skill to read a 
     markdown formatted table layout, the additional context could be an example
     table layout. This additional context is including in the YAML for the
     skill and not external to it. 

     > [!NOTE]
     > The content of the table layout will not be used in training
     > or aligning the model; only the table layout format itself will be used.

     Grounded skills include things like:
       * Game creation like Sudoku or tic tac toe
       * Count the number of punctuation marks in a paragraph
       * Find unresolved items in a meeting transcript

## Building Your LLM Intuition

LLMs have inherent limitations that make certain tasks extremely difficult, like doing math problems. They're great at other tasks, like creative writing. And they could be better at things like logical reasoning.

Consider these when you're generating skills. Skills in the first and second categories are welcomed. Skills in the third category are usually borderline and may be rejected.

### LLMs are great at

Skills in this category are welcomed, as refining these abilities helps us get better at the kinds of tasks where LLMs can excel.

For these, however, it's common for LLMs to already have excellent performance. Try 3-5 examples in `lab chat` to confirm a deficit in the model before you build your submission, and share the examples in your Pull Request (PR).

* Brainstorming
* Creativity
* Connecting information
* Cross-lingual behavior

### LLMs need help with

Skills in this category are welcomed, since LLM behavior in these sorts of topics are very difficult for the model to get right. Try several examples to understand the nuances of the model's ability to do these sorts of tasks, and consider using corrections to the results you get in your tuning process.

* Chains of reasoning
* Analysis
* Story plots
* Reassembling information
* Effective and succinct summaries

### LLMs are not so great at

Skills in this category are ways in which LLMs struggle, and may always struggle. Solving math and computation problems via probability on natural language queries is probably not the best way to solve them. That said, improving some of these foundational skills may be something this work tackles in the future, but not at this time.

Most skill submissions in these categories are likely to be rejected.

For hallucinations in particular, trying to solve this with a skill is unlikely to work. Consider contributing to the Knowledge taxonomy when it opens instead to improve the model's understanding of facts.

* Math
* Computation
* "Turing-complete" type tasks
* Generating only true real-world information (they're prone to hallucinations)

## Accepted Skills

### Creative Writing / Poetics

Adding new types of documents and writing styles to the LLM are welcome. Consider:

* Song lyrics
* Soliloquies
* Five paragraph essays
* Arguments

### Learning to Format Information

Skills to better format and reassemble information are helpful.

### Table Analysis and Processing

Consider:
* Drawing verbal inferences and conclusions about what's in a table
* Sorting
* Selecting
* Joining

### Qualitative Inference and Chain-of-Thought Reasoning

e.g.
> Mary is taller than John.
> John is taller than Anna.
> Is Anna taller than Mary?

e.g.
> An elephant, a mouse and a horse are in a room. How would they be ordered if they were standing in order by size?

Great skills in this category should include the correct line of reasoning in the answer, not just what the answer is.

### Word Problems

Is your LLM smarter than a second grader?

### Trust and Safety

Please avoid HAP (hate, abuse and profanity) and PII (personal identifiable information) in your examples.

Anything related to trust and safety will be flagged for higher-level review.


### Searching, Extraction and Summarization

Skills to select odd information in a document, draw conclusions, pull out information, draw insights or generate TODOs from information provided in the "Context" field are welcome.

### Complex Rulesets and Games

> [!NOTE]
> This is a good example of the need for a _grounded skill_. Grounded skills require the user to provide context containing information that the model is expected to take into account during processing. This is different from _knowledge_, where the model is expected to gain facts and background knowledge from the tuning process.
> 
> Context added when tuning a grounded skill would need to be again provided by the end user at inference time. The skill here is better adherence to the rule set.
 
To add a skill for a structured game or other task with a complex rule set, use a grounded skill.

Add the rules to the game as "context" in every example.

Add the interpretation as a question.

### Writing Style and Personalities

When adding a skill, expect that you're tuning a fairly general purpose LLM to behave better given particular circumstances.

If you want to add a skill to better adopt a particular personality - say, "a little boy living in the 1800s" - that context needs to be provided in either the "context" or "question" field.

### Instruction-Following Behavior

LLMs could be better at following extra instructions in a prompt about how to do a task, such as: "Keep your response to 200 words." Or: "Only produce 10 items." Skills to improve this behavior will help the model behave with more precision.

## Skills to Avoid

There are several types of skills that we don't expect this procedure to improve. Most skills in these categories will be rejected.

### Math

Trying to make the LLM solve math problems will be rejected.

### Real world knowledge-based skills

Unless it can be framed as a "grounded skill", where the user is expected to provide context, knowledge contributions will be a separate part of the taxonomy. Skills shouldn't expect the model to come up with its own facts, but instead assemble facts provided.

### Red Teaming

Adversarial questions and answers will be rejected at this time.

### Turing-complete style problems

These are an edge case, but things like palindromes and regexes, where getting the right answer with a non-stochastic program would be easy, aren't good targets for the moment.

Ask in the channel if you have an idea in this space before submitting a PR.

### Small Changes to Original Response

If the original LLM response is pretty close, but it's not responding to your exact expectations, a skill is not the right way to solve that problem.
