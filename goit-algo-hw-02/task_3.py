def is_bracket_sequence_symmetric(expression):
    """
    Check if a bracket sequence in the given expression is symmetric (balanced) using a stack.

    A sequence is considered symmetric if:
    - Every opening bracket has a matching closing bracket of the same type.
    - Brackets are properly nested and ordered.
    - Supported brackets: (), [], {}

    Parameters:
    expression (str): The string containing the bracket sequence.

    Returns:
    str: "Symmetric" if brackets are balanced, "Asymmetric" otherwise.
    """

    stack = []

    # Mapping of closing brackets to their corresponding opening brackets
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in bracket_pairs.values():
            # It's an opening bracket, push onto the stack
            stack.append(char)
        elif char in bracket_pairs:
            # It's a closing bracket, check for matching opening bracket
            if not stack:
                return "Asymmetric"  # Closing bracket without opening
            if stack[-1] == bracket_pairs[char]:
                stack.pop()  # Correct match, remove opening from stack
            else:
                return "Asymmetric"  # Mismatched pair

    # If stack is empty, all brackets matched
    return "Symmetric" if not stack else "Asymmetric"


if __name__ == "__main__":
    # Test cases to validate bracket symmetry checking
    test_expressions = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",  # Symmetric
        "( 23 ( 2 - 3);",             # Asymmetric
        "( 11 }",                     # Asymmetric
        "{ [ ( ) ] }",                # Symmetric
        "{ [ ( ] ) }",                # Asymmetric
        "(((())))",                   # Symmetric
        "(((())",                     # Asymmetric
        "( { [ ] } )",                # Symmetric
        "( [ ) ]",                    # Asymmetric
    ]

    for expression in test_expressions:
        result = is_bracket_sequence_symmetric(expression)
        print(f"{expression}: {result}")
