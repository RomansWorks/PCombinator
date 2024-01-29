![Build Status](https://img.shields.io/github/actions/workflow/status/RomansWorks/pcombinator/build-library)
![Coverage Status](https://img.shields.io/codecov/c/github/RomansWorks/pcombinator)
![GitHub](https://img.shields.io/github/license/RomansWorks/pcombinator)
![PyPI version](https://img.shields.io/pypi/v/pcombinator)
![Python version](https://img.shields.io/badge/python-3.10-blue.svg)


# PCombinator

## What is it?

PCombinator creates combinations of prompts from a tree of other combinators, and eventually string or None values at the leafes. It also stores the identifiers used to create the specific combination, for later evaluation of the effectiveness of each node in the tree. The evaluation functionality is not yet implemented.

There are several types of combinators:
1. TemplateCombinator: takes a template and a list of children, and fills the template with the children. The template is a string with slots to be filled by the children. The slots are identified by their name, which is the key in the dictionary of children. The template can also contain fixed strings, which are not filled by the children.
2. OneOfCombinator: takes a list of children, and returns one of them at random.
3. RandomJoinCombinator: takes a list of children, and returns a string which is the concatenation of a randomly selected and permuted subset of the children, with a separator between each child.
4. FixedStringCombinator: can be used in place of using a string leaf, to allow for storing an identifier in the IdTree.


1. Combines candidate prompts for LLMs from Ingredients and Alternatives, mixed within a Template according to probabilities.
2. Stores created prompts in a standardised format which is designed for use in later evaluation.
3. Load and get candidate prompts for evaluation.
4. (TODO): Evaluator given scores per prompt which helps detect the ingredients and alternatives which are most effective.

# Ingredients
Ingredients have a type to make it easier to evaluate which type of ingredient contributes most to the effectiveness of a prompt. The currently know best-practice types are to be recorded in best_practices.py. 


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
7. Add serialization for Combinators 
8. Decide if strings need an identifier in the IdTree for compatibility with the PromptBase library and PromptEvaluator. 
9. Normalize convention around internal fields.
10. Add support for encoding atoms such that they don't interfere with any separators.
11. Add support for random separators at least in random_join_combinator.


# Developing

## Setup

`poetry install -E templating --no-root`

## Testing

`poetry run pytest`

## Building the distribution

`poetry build`
