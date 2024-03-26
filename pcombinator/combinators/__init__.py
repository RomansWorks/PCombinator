# import os
# import glob

# # Get the current directory
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # Get all Python files in the current directory
# files = glob.glob(os.path.join(current_dir, "*.py"))

# # Initialize the __all__ list
# __all__ = []

# # Iterate over the files
# for file in files:
#     # Exclude the current file
#     if file != __file__:
#         # Get the module name from the file name
#         module_name = os.path.splitext(os.path.basename(file))[0]

#         # Import the module
#         module = __import__(module_name, globals(), locals(), [], 0)

#         # Get the names of the combinator types defined in the module
#         combinator_types = [name for name in dir(module) if name.startswith("Type")]

#         # Add the combinator types to the __all__ list
#         __all__.extend(combinator_types)
