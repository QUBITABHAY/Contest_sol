import math

# Function to check if a number is a perfect power of some integer k
def is_perfect_power(ratio):
    if ratio == 1:
        return True  # 1 is a perfect power (1^n for any n)
    
    # Check for integer k and n such that k^n == ratio
    for k in range(2, int(math.sqrt(ratio)) + 1):
        # Try to find n such that k^n == ratio
        power = k
        while power < ratio:
            power *= k
        if power == ratio:
            return True
    return False

# Main function to check if y/x is a perfect power
def check_ratio_is_power(y, x):
    if y % x != 0:
        return "NO"  # y/x is not an integer
    ratio = y // x  # Integer result of y/x
    if is_perfect_power(ratio):
        return "YES"
    else:
        return "NO"

# Read number of test cases
t = int(input())  # Number of test cases

# Process each test case
for _ in range(t):
    y, x = map(int, input().split())  # Read y and x
    print(check_ratio_is_power(y, x))  # Check and print result


# Wrong code ^^^^^^^^^^