# What is the Path

The Path represents the specific identifiers used at each node in the tree to create a specific prompt. Essentially the "bill of materials".

## Applications 

With a Path object you can:
1. Render the prompt (using the `render_path` method of a combinator)
2. Associate the ingredients of the prompt with an evaluation metric to measure the individual contribution of each ingredient to the effectiveness of the prompt.
3. Replace parts of the path dynamically in runtime, for example injecting (retrieval) augmentation info into the prompt, changing rules based on user's permissions and context, and more.

## Example Path

The following path is taken from the (example)[../examples/text2text/example.py]:

```json
{
  "root": {
    "role": {
      "role_combinator": {
        "1": {
          "2": {}
        }
      }
    },
    "task": {
      "task_combinator": {
        "1": "Your task is to explain concepts provided by the user on three levels - beginner, intermediate, expert."
      }
    },
    "tone": {
      "tone_combinator": {
        "1": "Use clean and professional tone."
      }
    },
    "step_by_step": {
      "step_by_step_combinator": {
        "0": "Use the following step by step instruction to answer the user query:\nStep 1: Rephrase the user question or request.\nStep 2: Answer the question or request.\n"
      }
    },
    "tip": {
      "tip_combinator": {
        "1": "I'm going to tip $10 for a perfect response!"
      }
    },
    "examples": {
      "examples_combinator": {
        "2": {
          "2": {}
        },
        "0": {
          "0": {}
        }
      }
    }
  }
}
```

The same tree of combinators will deterministically render the same output prompt when given the same path. 

This path matches the following prompt:

```
You're an expert teacher with creative approach to explaining.
Your task is to explain concepts provided by the user on three levels - beginner, intermediate, expert.
Use clean and professional tone.
Use the following step by step instruction to answer the user query:
Step 1: Rephrase the user question or request.
Step 2: Answer the question or request.

I'm going to tip $10 for a perfect response!
Examples:
====
Question: Get the top 10 customers by revenue
Answer: SELECT * FROM customers ORDER BY revenue DESC LIMIT 10
Question: Get all records from the employees table
Answer: SELECT * FROM employees 
```

Please see and run the (example)[../examples/text2text/example.py] to see the full flow. 

# How the Path is constructed

The Path is a Bill of Materials - it identifies what elements went into the prompt, and in what order. 

We use the Path for two purposes:
1. When comparing prompts, this allows analysis of the contribution of different elements to the effectiveness of the prompt.
2. When replacing parts of the prompt dynamically in runtime. 

Paths are returned by the `generate_paths()` method of combinators. a Path is built as following:
1. It contains a single key, the `id` of the Combinator, and a value listing the Path for each of the children.
2. The Paths of its children can be a list or a dictionary, depending on the combinator. For template combinator, we want to associate the child with the template slot it fills, so we use a dictionary with the slot name as key and the path as the value. For the other combinators, we just want to list the children, so we use a list.
3. Combinators also accept strings an None values as (leaf) children, in which case for now we don't store any identifier in the Path. If you do want to store an identifier, use the `NameString` combinator instead of the string. 
