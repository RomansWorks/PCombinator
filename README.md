# LLMPromptComposer

1. Combines candidate prompts for LLMs from Ingredients and Alternatives, mixed within a Template according to probabilities.
2. Stores created prompts in a standardised format which is designed for use in later evaluation.
3. Load and get candidate prompts for evaluation.
4. (TODO): Evaluator given scores per prompt which helps detect the ingredients and alternatives which are most effective.

# Ingredients
Ingredients have a type to make it easier to evaluate which type of ingredient contributes most to the effectiveness of a prompt. The currently know best-practice types are to be recorded in best_practices.py. 


# TODO: 
1. Eliminate duplicates when generating prompts
2. Add a filter callback the user can use to disapprove of prompts (for example prompts are too similar to others already generated or attempted, too short, too long, contradictory in ingredients, etc)
3. Add limit to number of selection attempts (since some selections will fail due to duplicates and filter, we want to allow limitied attempts to find a valid prompt)
4. Consider allowing nesting ingredients
5. Add best_practices.py file with example ingredients which can be copied into the user's own file
6. Additional examples
7. Additional documentation
8. Tests
9. Separators alternatives
10. How can templating be made more flexible such as to include weight for ingredient selection in the template?
11. Supoprt for always included variants and ingredients