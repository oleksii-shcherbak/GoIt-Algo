from collections import deque


def is_palindrome(input_string):
    """
    Determine whether a given string is a palindrome using a deque.

    A palindrome is a string that reads the same forwards and backwards.
    This function:
    - Ignores spaces
    - Is case-insensitive
    - Uses a deque to efficiently compare characters from both ends

    Parameters:
    input_string (str): The string to be checked.

    Returns:
    bool: True if the input string is a palindrome, False otherwise.
    """

    # Normalize the string: remove all whitespace and convert to lowercase
    normalized = ''.join(char.lower() for char in input_string if not char.isspace())

    # Create a deque from the normalized string
    char_deque = deque(normalized)

    # Compare characters from both ends until the deque is empty or mismatch is found
    while len(char_deque) > 1:
        left = char_deque.popleft()
        right = char_deque.pop()
        if left != right:
            return False  # Mismatch found

    return True  # All characters matched


if __name__ == "__main__":
    # Test cases for the palindrome checker
    test_strings = [
        "A man a plan a canal Panama",
        "racecar",
        "Was it a car or a cat I saw",
        "hello",
        "Never odd or even"
    ]

    for test_input in test_strings:
        result = is_palindrome(test_input)
        print(f"'{test_input}' -> Palindrome: {result}")
