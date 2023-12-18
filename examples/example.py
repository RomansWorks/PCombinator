from typing import List
import src.prompt_combinator as pc
from src.types import Ingredient

def main():
    ingredients : List[Ingredient]= [
        Ingredient(
            type="role",
            weight=0.5,
            variants=[
                { "value": "You're a highly precise language model assistant.", "weight": 0.5 },
                { "value": "You're an expert teacher with creative approach to explaining.", "weight": 0.5 }
            ]
        ),
        Ingredient(
            type="task",
            weight=0.5,
            variants=[
                { "value": "Your task is to explain concepts provided by the user on three levels - ELI5, intuitive and rigorous", "weight": 0.5 },
                { "value": "Your task is to explain concepts provided by the user on three levels - beginner, intermediate, expert", "weight": 0.5 },
                { "value": "Your task is to explain concepts provided by the user on three levels", "weight": 0.5 }
            ]
        ),
        Ingredient(
            type="tone",
            weight=0.5,
            variants=[
                { "value": "Use a friendly and supporive tone", "weight": 0.5 },
                { "value": "Use clean and professional tone", "weight": 0.5 }
            ]
        ),
        Ingredient(
            type="step_by_step",
            weight=0.5,
            variants=[
                { "value": """Use the following step by step instruction to answer the user query:
                 Step 1: Rephrase the user question or request.
                 Step 2: Answer the question or request.
                 """, "weight": 0.5 },
                { "value": """
                            Follow these steps when answering the user query:
                            Step 1: Briefly rephrase the user question or request.
                            Step 2: Answer the question or request.
                            """, "weight": 0.5 }
            ]
        )
    ]

    
    templates = [



# Main
if __name__ == "__main__":
    main()