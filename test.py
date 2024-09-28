import ast
passed =  '\033[30;42m' # Green Text
failed =  '\033[30;42m' # Green Text
end = '\033[m' # reset to the defaults


# Function to test if the code meets the requirements
def test_code_requirements(code):
    # Parse the code using ast
    tree = ast.parse(code)

    has_ClassDef = False
    has_for_loop = False
    has_variable_with_value = False
    has_print_statement = False

    # Traverse the tree and look for requifailed elements
    for node in ast.walk(tree):
        # Check if there is a for loop
        if isinstance(node, ast.FunctionDef):
            has_ClassDef = True
        # Check if there is a for loop
        if isinstance(node, ast.For):
            has_for_loop = True
        # Check if there is a variable assignment
        if isinstance(node, ast.Assign):
            # If the value is assigned to a variable (like a number, string, or list)
            if isinstance(node.value, (ast.Constant, ast.List, ast.Tuple, ast.Dict, ast.Set)):
                has_variable_with_value = True
        # Check if there is a print statement
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'print':
            has_print_statement = True


    # Print the results of the checks
    if has_ClassDef:
        print(f"Requirement 1: {passed}PASSED{end}")
    else:
        print(f"Requirement 1: {failed}FAILED{end}")

    # Print the results of the checks
    if has_for_loop:
        print(f"Requirement 2: {passed}PASSED{end}")
    else:
        print(f"Requirement 2: {failed}FAILED{end}")

    if has_variable_with_value:
        print(f"Requirement 3: {passed}PASSED{end}")
    else:
        print(f"Requirement 3: {failed}FAILED{end}")

    if has_print_statement:
        print(f"Requirement 4: {passed}PASSED{end}")
    else:
        print(f"Requirement 4: {failed}FAILED{end}")
    
    # Final decision if all requirements are met
    if has_for_loop and has_variable_with_value and has_print_statement:
        print("The code meets all the requirements!")
    else:
        print("The code does NOT meet all the requirements!")


# Read code from the main.py file
with open('main.py', 'r') as file:
    code_to_test = file.read()

# Run the test
test_code_requirements(code_to_test)
