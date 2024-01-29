from dataclasses import dataclass
from pcombinator.combinators.combinator import Combinator
import json


@dataclass
class CombinatorsFile:
    version: str
    seed: int
    root_combinator: Combinator

    def to_pickle(self, path: str) -> None:
        import pickle

        with open(path, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def from_pickle(path: str) -> "CombinatorsFile":
        import pickle

        with open(path, "rb") as f:
            return pickle.load(f)

    def to_json(self):
        return {
            "version": self.version,
            "seed": self.seed,
            "root_combinator": self.root_combinator.to_json(),
        }

    def to_json_file(self, path: str) -> None:
        with open(path, "w") as f:
            json.dump(self.to_json(), f)

    @staticmethod
    def from_json_file(path: str) -> "CombinatorsFile":
        with open(path, "r") as f:
            return CombinatorsFile(**json.load(f))
