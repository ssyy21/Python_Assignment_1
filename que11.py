# 11. Write a python program that generates the first n numbers in the Fibonacci sequence.
def fibonacci_sequence(n):
    a, b = 0, 1
    result = []
    while a <= n:
        result.append(a)
        a, b = b, a + b
    return result

n = int(input("Enter the value of n: "))
fib_sequence = fibonacci_sequence(n)
print("Fibonacci sequence up to", n, ":", fib_sequence)
