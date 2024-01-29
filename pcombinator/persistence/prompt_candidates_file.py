import json
from dataclasses import dataclass
from typing import Annotated, Dict, List, Union

from pydantic import BaseModel, Field

from pcombinator.combinators.combinator import Combinator, IdTree
from pcombinator.combinators.tests.test_template_combinator import (
    TemplateCombinatorTests,
)
from pcombinator.combinators.fixed_string_combinator import FixedStringCombinator
from pcombinator.combinators.one_of_combinator import OneOfCombinator
from pcombinator.combinators.random_join_combinator import RandomJoinCombinator


@dataclass
class PromptCandidatesFile(BaseModel):
    version: str
    seed: int
    root_combinator: Annotated[
        Union[
            FixedStringCombinator,
            OneOfCombinator,
            RandomJoinCombinator,
            TemplateCombinatorTests,
        ],
        Field(discriminator="duck_type"),
    ]

    generated_prompts: List[Dict[str, IdTree]]

    def to_pickle(self, path: str) -> None:
        import pickle

        with open(path, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def from_pickle(path: str) -> "PromptCandidatesFile":
        import pickle

        with open(path, "rb") as f:
            return pickle.load(f)

    def to_json(self, path: str) -> None:
        json = self.model_dump_json()
        with open(path, "w") as f:
            f.write(json)

    @staticmethod
    def from_json(path: str) -> "PromptCandidatesFile":
        with open(path, "r") as f:
            json = f.read()
            return "PromptCandidatesFile".parse_raw(json)
