from dataclasses import dataclass
from typing import List, Mapping

type IngredientType = str

@dataclass
class Variant:
    value: str
    weight: float
    

@dataclass
class Ingredient:
    type: IngredientType
    weight: float
    variants: List[Variant]


# @dataclass
# class Separator:
#     text: str
#     weight: float

@dataclass
class PromptCandidate:
    text: str
    template_id: str
    ingredients_used: Mapping[IngredientType, str]
