def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
fibonacci_sequence = generate_fibonacci(num_terms)
print("Fibonacci Sequence:")
print(fibonacci_sequence)
