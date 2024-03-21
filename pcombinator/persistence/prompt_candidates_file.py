import json
from dataclasses import dataclass
from typing import Annotated, Dict, List, Union


from pcombinator.combinators.combinator import Combinator, IdTree
from pcombinator.combinators.tests.test_template_combinator import (
    TemplateCombinatorTests,
)
from pcombinator.combinators.fixed_string_combinator import FixedStringCombinator
from pcombinator.combinators.one_of_combinator import OneOfCombinator
from pcombinator.combinators.some_of_combinator import SomeOfCombinator


@dataclass
class PromptCandidatesFile:
    version: str
    seed: int
    root_combinator: Annotated[
        Union[
            FixedStringCombinator,
            OneOfCombinator,
            SomeOfCombinator,
            TemplateCombinatorTests,
        ],
        # Field(discriminator="duck_type"),
        None,  # Temporary
    ]

    generated_prompts: List[Dict[str, IdTree]]

    def to_pickle(self, path: str) -> None:
        """
        Save the object to a pickle file.
        NOTE: pickle files are unsafe to load. Only load pickle files from trusted sources.
        """
        import pickle

        with open(path, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def from_pickle(path: str) -> "PromptCandidatesFile":
        """
        Load the object from a pickle file.
        NOTE: pickle files are unsafe to load. Only load pickle files from trusted sources.
        """
        import pickle

        with open(path, "rb") as f:
            return pickle.load(f)

    def to_json(self) -> str:
        return json.dumps(
            {
                "version": self.version,
                "seed": self.seed,
                "root_combinator": self.root_combinator.to_json(),
                "generated_prompts": self.generated_prompts,
            }
        )

    def to_json_file(self, path: str) -> None:
        json = self.to_json()
        with open(path, "w") as f:
            f.write(json)

    @staticmethod
    def from_json(path: str) -> "PromptCandidatesFile":
        with open(path, "r") as f:
            json = f.read()
            return "PromptCandidatesFile".parse_raw(json)
