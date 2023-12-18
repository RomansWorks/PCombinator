from typing import List
import random

from src.types import Ingredient, Template, Variant


def normalize_template_probabilities(templates: List[Template]) -> List[Template]:
    weight_sum = sum([template.weight for template in templates])
    templates_copy = templates.copy()
    for template in templates_copy:
        template.weight = template.weight / weight_sum
    return templates_copy


def select_template_weighted(templates: List[Template]) -> Template:
    probabilities = [template.weight for template in templates]
    return random.choices(templates, weights=probabilities, k=1)[0]


def normalize_ingredient_probabilities(
    required_ingredients: List[Ingredient],
) -> List[Ingredient]:
    weight_sum = sum([ingredient.weight for ingredient in required_ingredients])
    ingredients_copy = required_ingredients.copy()
    for ingredient in ingredients_copy:
        ingredient.weight = ingredient.weight / weight_sum
    return ingredients_copy


def select_ingredients_weighted(
    required_ingredients: List[Ingredient], k: int | None
) -> List[Ingredient]:
    """
    Selects k ingredients from required_ingredients by normalized weight.
    If k is None, selects all ingredients.
    """
    probabilities = [ingredient.weight for ingredient in required_ingredients]
    return random.choices(
        required_ingredients, weights=probabilities, k=k or len(required_ingredients)
    )[0]


def select_variant_weighted(variants: List[str]) -> Variant:
    weights = [variant.weight for variant in variants]
    return random.choices(variants, weights=weights, k=1)[0]
