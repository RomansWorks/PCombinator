import random
from typing import List
from src.choice_utils import (
    find_required_ingredients,
    normalize_ingredient_probabilities,
    normalize_template_probabilities,
    select_ingredients_weighted,
    select_template_weighted,
    select_variant_weighted,
)

from src.types import Ingredient, Template, PromptCandidate


def combine_prompts_using_templates(
    ingredients: List[Ingredient], templates: List[Template], max_candidates: int
) -> List[PromptCandidate]:
    if len(ingredients) == 0:
        raise ValueError("No ingredients provided")
    if len(templates) == 0:
        raise ValueError("No templates provided")
    if max_candidates < 1:
        raise ValueError("max_candidates must be at least 1")

    # Normalize templates probabilities
    # TODO: Is this strictly necessary? random.choices() can take non-normalized weights
    normalized_templates = normalize_template_probabilities(templates)

    candidates = []
    for i in range(max_candidates):
        # Per candidate prompt, choose a template among templates by normalized weight
        selected_template = select_template_weighted(normalized_templates)

        # Given the template, find which ingredients it requires
        required_ingredient_types = selected_template.get_required_ingredient_types()

        # Normalize probabilities on the side for the specific ingredients
        required_ingredients = [
            ingredient
            for ingredient in ingredients
            if ingredient.type in required_ingredient_types
        ]

        # Select a variant for each ingredient
        selected_variants = {}
        for ingredient in required_ingredients:
            selected_variant = select_variant_weighted(ingredient.variants)
            selected_variants.set(ingredient.type, selected_variant.value)

        # Embed into template
        prompt = selected_template.build_prompt(selected_variants)

        # Add to candidates
        candidates.append(prompt)

    # Return
    return candidates


def combine_prompts_using_random(
    ingredients: List[Ingredient], max_candidates: int
) -> List[PromptCandidate]:
    if len(ingredients) == 0:
        raise ValueError("No ingredients provided")
    if max_candidates < 1:
        raise ValueError("max_candidates must be at least 1")

    # Normalize ingredients probabilities
    normalized_ingredients = normalize_ingredient_probabilities(ingredients)

    # Per candidate prompt
    candidates = []
    for i in range(max_candidates):
        # Per candidate prompt, choose a number of ingredients to include
        required_ingredients = select_ingredients_weighted(normalized_ingredients)

        # Combine randomly into a prompt
        random.shuffle(required_ingredients)
        prompt_text = ""
        for ingredient in required_ingredients:
            variant = select_variant_weighted(ingredient.variants)
            prompt_text += variant
            if prompt_text[-1] != ".":
                prompt_text += ". "

        # Strip the trailing ". "
        if prompt_text[-2:] == ". ":
            prompt_text = prompt_text[:-2]

        # Add to candidates
        candidates.append(
            PromptCandidate(
                text=prompt_text, template_id="random", ingredients=required_ingredients
            )
        )

    # Return
    return candidates
