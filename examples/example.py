from typing import List
from pcombinator.combinators.join_some_of import JoinSomeOf
from pcombinator.combinators.named_string import NamedString
from pcombinator.combinators.jinja2_template import Jinja2Template
from pcombinator.combinators.pick_one import PickOne

import json
from rich import print, print_json


def main():

    # This example picks one named string of several
    # Named strings preserve the id in the IdTree, while regular strings do not
    role_combinator = PickOne(
        id="role_combinator",
        children=[
            NamedString(
                id="1", string="You're a highly precise language model assistant."
            ),
            NamedString(
                id="2",
                string="You're an expert teacher with creative approach to explaining.",
            ),
        ],
    )

    # This example picks one string of several
    task_combinator = PickOne(
        id="task_combinator",
        children=[
            "Your task is to explain concepts provided by the user on three levels - ELI5, intuitive and rigorous.",
            "Your task is to explain concepts provided by the user on three levels - beginner, intermediate, expert.",
            "Your task is to explain concepts provided by the user on three levels.",
        ],
    )

    tone_combinator = PickOne(
        id="tone_combinator",
        children=[
            "Use a friendly and supporive tone.",
            "Use clean and professional tone.",
            None,
        ],
    )

    step_by_step_combinator = PickOne(
        id="step_by_step_combinator",
        children=[
            """Use the following step by step instruction to answer the user query:
Step 1: Rephrase the user question or request.
Step 2: Answer the question or request.
""",
            """Follow these steps when answering the user query:
Step 1: Briefly rephrase the user question or request.
Step 2: Answer the question or request.
""",
            "Think step by step.",
            None,
        ],
    )

    # Example of generating a list of samples from a dict, and combining some of them with a separator
    examples_list = [
        {
            "question:": "Get all records from the employees table",
            "answer": "SELECT * FROM employees",
        },
        {
            "question:": 'Get the single customer with id "PCombinator"',
            "answer": "SELECT DISTINCT * FROM customers WHERE id = 'PCombinator'",
        },
        {
            "question:": "Get the top 10 customers by revenue",
            "answer": "SELECT * FROM customers ORDER BY revenue DESC LIMIT 10",
        },
    ]

    example_strings = [
        f"Question: {example['question:']}\nAnswer: {example['answer']}"
        for example in examples_list
    ]
    example_named_strings = [
        NamedString(id=str(idx), string=example)
        for idx, example in enumerate(example_strings)
    ]

    examples_combinator = JoinSomeOf(
        id="examples_combinator",
        n_min=1,
        n_max=3,
        separator="\n",
        children=example_named_strings,
    )

    # This example is for using a Jinja2 template to combine the strings
    root_combinator = Jinja2Template(
        id="root",
        template_source="""
{{ role }}
{{ task }}
{{ tone }}
{{ step_by_step }}
Examples:
{{ examples }}
""",
        children={
            "role": role_combinator,
            "task": task_combinator,
            "tone": tone_combinator,
            "step_by_step": step_by_step_combinator,
            "examples": examples_combinator,
        },
    )

    paths = root_combinator.generate_paths()
    n_samples = 5
    for idx in range(n_samples):
        path = paths[idx]
        rendered_prompt = root_combinator.render_path(path)
        print(
            f"\U000027A1 [bold blue] Candidate prompt [/bold blue][bold white]{idx}[/bold white]: "
        )
        print(f"[yellow] {rendered_prompt} [/yellow]")
        print()
        print(
            f"\U000027A1 [bold blue] Candidate ingredients (IdTree) for prompt [/bold blue][bold white]{idx}[/bold white]:"
        )
        pretty_path = json.dumps(path, indent=2)
        print_json(pretty_path)
        print("=" * 80)


# Main
if __name__ == "__main__":
    main()
