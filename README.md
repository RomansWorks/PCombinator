# PCombinator

1. Combines candidate prompts for LLMs from Ingredients and Alternatives, mixed within a Template according to probabilities.
2. Stores created prompts in a standardised format which is designed for use in later evaluation.
3. Load and get candidate prompts for evaluation.
4. (TODO): Evaluator given scores per prompt which helps detect the ingredients and alternatives which are most effective.

# Ingredients
Ingredients have a type to make it easier to evaluate which type of ingredient contributes most to the effectiveness of a prompt. The currently know best-practice types are to be recorded in best_practices.py. 


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


Fix:
1. Does render add own id to the id tree or does the render_children add it for the children?
2. How do Ids and keys work together in the idtree?
