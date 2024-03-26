# Setup

`poetry install -E templating --no-root`

# Testing

`poetry run pytest`

# Building the distribution

`poetry build`

# Ideas for refactoring

1. See if we can unify the model of children being either a list or a dict, and create generic rendering methods with specific callbacks for each case.
