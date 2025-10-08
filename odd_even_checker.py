def check_odd_even(number):
    """
    Checks if a given integer is odd or even.

    The determination is based on the modulus operator (%), which returns 
    the remainder of a division. If the remainder when dividing by 2 is 0, 
    the number is even.

    Args:
        number (int): The integer to check.

    Returns:
        str: A message indicating whether the number is "Even" or "Odd".
             Returns an error message for non-integer input.
    """
    # 1. Input Validation
    # Ensure the input is an integer
    if not isinstance(number, int):
        return "Error: Input must be an integer."

    # 2. Odd/Even Logic
    if number % 2 == 0:
        return f"{number} is Even."
    else:
        return f"{number} is Odd."

# --- Example Usage ---

if __name__ == "__main__":
    
    # Test Cases
    num1 = 14
    num2 = 7
    num3 = 0
    num4 = -11
    num_invalid = 10.5

    print(check_odd_even(num1))
    print(check_odd_even(num2))
    print(check_odd_even(num3))
    print(check_odd_even(num4))
    print(check_odd_even(num_invalid))
