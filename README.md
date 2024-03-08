![Build Status](https://img.shields.io/github/actions/workflow/status/RomansWorks/PCombinator/build-library)
![Coverage Status](https://img.shields.io/codecov/c/github/RomansWorks/PCombinator)
![GitHub](https://img.shields.io/github/license/RomansWorks/PCombinator)
![PyPI version](https://img.shields.io/pypi/v/Pcombinator)
![Python version](https://img.shields.io/badge/python-3.10-blue.svg)


# PCombinator

A handy tool for generating variations of prompts for large language and vision models, and evaluating the effectiveness of each particle in the variation. With it you can systematically optimize your prompts. 

Some examples of questions you can easily test using PCombinator:
- Is giving a an example (few shot) to the prompt contributes to effectiveness? 
- Is a specific example or combination of examples better than the others?
- Is this additional instruction helpful?
- Is putting the examples before the rules or instructions better, or is it vice versa?
- Which delimiter is the best for separating examples? (see )
- Does Chain of Though (CoT) help or just cost more?
- Does the order of the examples matter?
- Do I need this many examples?
- Should I use an instructive language or a more conversational one?
- Is a certain role for the model biases it better than another role?
- Which terms in a text2image prompt contribute more to the effectiveness of the prompt?

There are two parts to the library, each can be used independently:
1. The Combinators (arranged in a tree): which generate the prompts.
2. The Evaluator: which evaluates the effectiveness of the prompts.

Some metrics that can be used to evaluate the effectiveness of the prompts:
- The score given by a human or a model judge to the output. 
- Use existing labeled datasets and evaluators 
- The perplexity of the model on the prompt. 

## How to use it?

### Generating candidates

```python
from pcombinator import TemplateCombinator, OneOfCombinator, RandomJoinCombinator, FixedStringCombinator

# Create the combinators
template = TemplateCombinator(
    "This is a template with {child1} and {child2}.",
    children={
        "child1": OneOfCombinator(
            children=[
                FixedStringCombinator("child1a"),
                FixedStringCombinator("child1b"),
            ]
        ),
        "child2": RandomJoinCombinator(
            children=[
                FixedStringCombinator("child2a"),
                FixedStringCombinator("child2b"),
            ],
            separator=" or ",
        ),
    },
)

# # Save the combinator tree for future use
# json_str = template_combinator.to_json()
# with open("path/to/combinator.json", "w") as f:
#     f.write(json_str)

# # Loading the combinator tree looks as following:
# with open("path/to/combinator.json", "r") as f:
#     json_str = f.read()
#     loaded_combinator = Combinator.from_json(json_str)


# Render 10 different versions of the resulting prompt:
for _ in range(10):
    prompt, id_tree = template.render()
    print("=" * 80)
    print(prompt)
    print("-" * 80)
    print(id_tree)


# Save the prompt and id_tree for later evaluation
# TODO

***
```

See additional exampels in the `examples` folder and under `pcombinator/combinators/tests`.

### Evaluating candidates (not yet implemented)
```python

from pcombinator import load_candidates

# Load the candidates
candidates = load_candidates("path/to/candidates")

# Evaluate the candidates
scores = evaluate_candidates(candidates)

print(scores)
```

## What is it?

PCombinator creates combinations of prompts from a tree of other combinators, and eventually string or None values at the leaves. It also stores the identifiers used to create the specific combination, for later evaluation of the effectiveness of each node in the tree. The evaluation functionality is not yet implemented.

There are several types of combinators:
1. TemplateCombinator: takes a template and a list of children, and fills the template with the children. The template is a string with slots to be filled by the children. The slots are identified by their name, which is the key in the dictionary of children. The template can also contain fixed strings, which are not filled by the children.
2. OneOfCombinator: takes a list of children, and returns one of them at random.
3. RandomJoinCombinator: takes a list of children, and returns a string which is the concatenation of a randomly selected and permuted subset of the children, with a separator between each child.
4. FixedStringCombinator: can be used in place of using a string leaf, to allow for storing an identifier in the IdTree.


1. Combines candidate prompts for LLMs and multimodal models, mixed from a tree of Combinators.
2. Stores created prompts in a standardised format which is designed for use in later evaluation.
3. Save and Load combinator trees and rendered prompts for evaluation.
4. (TODO): Evaluator given scores per prompt which helps detect the contribution of each leaf value.


# IdTree

The IdTree identifies what elements went into the prompt. This is useful for later analysis of the contribution of different elements to the effectiveness of the prompt.

IdTree is returned by the `render()` method of combinators. It is built as following:
1. It contains a single key, the `id` of the Combinator, and a value listing the IdTrees of the children.
2. The IdTrees of its children can be a list or a dictionary, depending on the combinator. For template combinator, we want to associate the child with the template slot it fills, so we use a dictionary. For the other combinators, we just want to list the children, so we use a list.
3. Combinators also accept strings as children, in which case for now we don't store any identifier in the IdTree. If you do want to store an identifier, use the `FixedStringCombinator` instead of the string. 

# TODO: 
1. Implement best practices templates   
2. Duplication elimination at the top level, max attempts
3. Add methods documentation
4. Add general documentation
5. Add tests
6. Add examples
7. Decide if strings need an identifier in the IdTree for compatibility with the PromptBase library and PromptEvaluator. 
8. Normalize convention around internal fields.
9. Add support for encoding atoms such that they don't interfere with any separators.


# Developing

## Setup

`poetry install -E templating --no-root`

## Testing

`poetry run pytest`

## Building the distribution

`poetry build`
