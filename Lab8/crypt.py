# Write python code for arithmetic problem CROSS + ROADS = DANGER

def solve_cryptarithmetic(lhs, rhs, result):
    letters = set(lhs + rhs + result)
    if len(letters) > 10:
        print("Error: Too many unique letters for a cryptarithmetic problem (maximum 10)")
        return None

    def backtrack(idx, used_digits):
        if idx == len(letters):
            lhs_value = sum(used_digits[char] * (10 ** (len(lhs) - i - 1)) for i, char in enumerate(lhs))
            rhs_value = sum(used_digits[char] * (10 ** (len(rhs) - i - 1)) for i, char in enumerate(rhs))
            result_value = sum(used_digits[char] * (10 ** (len(result) - i - 1)) for i, char in enumerate(result))
        
            return lhs_value + rhs_value == result_value
        for digit in range(10):
            if digit not in used_digits.values():
                used_digits[list(letters)[idx]] = digit
                if backtrack(idx + 1, used_digits):
                    return True
                used_digits[list(letters)[idx]] = None
        return False

    used_digits = {letter: None for letter in letters}
    if backtrack(0, used_digits):
        return {letter: digit for letter, digit in used_digits.items() if digit is not None}
    else:
        return None

lhs, rhs, result = "SEND", "MORE", "MONEY"
solution = solve_cryptarithmetic(lhs, rhs, result)
if solution:
    print("Solution found:")
    for letter, value in solution.items():
        print(f"{letter}: {value}")
else:
    print("No solution found.")