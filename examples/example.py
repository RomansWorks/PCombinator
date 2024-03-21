from typing import List
from pcombinator.combinators.fixed_string_combinator import FixedStringCombinator
from pcombinator.combinators.template_combinator import Jinja2TemplateCombinator
from pcombinator.combinators.one_of_combinator import OneOfCombinator


def main():
    role_combinator = OneOfCombinator(
        id="role",
        children=[
            FixedStringCombinator(
                id="1", string="You're a highly precise language model assistant."
            ),
            FixedStringCombinator(
                id="2",
                string="You're an expert teacher with creative approach to explaining.",
            ),
        ],
    )

    task_combinator = OneOfCombinator(
        id="task",
        children=[
            "Your task is to explain concepts provided by the user on three levels - ELI5, intuitive and rigorous.",
            "Your task is to explain concepts provided by the user on three levels - beginner, intermediate, expert.",
            "Your task is to explain concepts provided by the user on three levels.",
        ],
    )

    tone_combinator = OneOfCombinator(
        id="tone",
        children=[
            "Use a friendly and supporive tone.",
            "Use clean and professional tone.",
            None,
        ],
    )

    step_by_step_combinator = OneOfCombinator(
        id="step_by_step",
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

    root_combinator = Jinja2TemplateCombinator(
        id="root",
        template_source="""
        {{ role }}
        {{ task }}
        {{ tone }}
        {{ step_by_step }}
        """,
        children={
            "role": role_combinator,
            "task": task_combinator,
            "tone": tone_combinator,
            "step_by_step": step_by_step_combinator,
        },
    )

    n_samples = 5
    for idx in range(n_samples):
        rendered, id_tree = root_combinator.render_any()
        print(f"Candidate {idx}:", rendered)
        print("Id tree:", id_tree)
        print()


# Main
if __name__ == "__main__":
    main()
