# Function to generate Fibonacci sequence using DFS
def fibonacci_dfs(n):
    # Base cases for Fibonacci sequence
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        # Initialize Fibonacci sequence with first two numbers
        sequence = [0, 1]
        # Perform DFS to generate Fibonacci sequence
        def dfs(prev1, prev2, count):
            if count == n:
                return
            next_num = prev1 + prev2
            sequence.append(next_num)
            dfs(prev2, next_num, count + 1)
        dfs(0, 1, 2)
        return sequence

# Example usage
n = 10
fib_sequence = fibonacci_dfs(n)
print(f"Fibonacci sequence of length {n}: {fib_sequence}")

