def correct_19(s: str) -> bool:
    """
    Check if the brackets in the input string are balanced.

    Parameters:
    - s (str): The input string containing brackets.

    Returns:
    bool: True if the brackets are balanced, False otherwise.
    """
    bracket_mapping = {"]": "[", "}": "{", ")": "("}
    stack = []

    for char in s:
        if char in bracket_mapping.values():
            stack.append(char)
        elif char in bracket_mapping.keys():
            if not stack or bracket_mapping[char] != stack.pop():
                return False
        else:
            return False

    return not stack
