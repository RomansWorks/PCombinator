    
from dataclasses import dataclass
from typing import List
from src.templates import Template

from src.types import Ingredient, PromptCandidate


@dataclass
class PromptCandidatesFile:
    version: str
    seed: int
    ingredients: List[Ingredient]
    templates: List[Template]
    # separators: List[Separator]

    candidates: List[PromptCandidate]
