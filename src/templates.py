from dataclasses import dataclass
from string import Template as StringTemplate
from typing import Mapping

from src.types import PromptCandidate

@dataclass
class Template:
    id: str
    string_template: StringTemplate
    weight: float

    def get_required_ingredient_types(self):
        return self.string_template.get_identifiers()
    
    def build_prompt(self, values: Mapping[str, str]) -> PromptCandidate:
        prompt_text = self.string_template.substitute(values)
        return PromptCandidate(
            text=prompt_text,
            template_id=self.id,
            ingredients=values
        )


