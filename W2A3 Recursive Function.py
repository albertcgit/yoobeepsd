import math

# my function for generating fibonacci series (recursive version)
def fibonacci(n): # compute a single Fibonacci number
    if n <= 1:  # Setting base values for F(0) and F(1)
        return n
    # Recursive calls to get next values
    return fibonacci(n - 1) + fibonacci(n - 2)

def generate_fibonacci(n):  # my function for generating fibonacci series

    if n <= 0:
        return []
    if n == 1:
        return [0]  # Setting base value for F(0)
    if n == 2:
        return [0, 1]  # Setting base values for F(0) and F(1)

    # Generate sequence until F(length-1) and return
    previous_term = generate_fibonacci(n - 1)
    next_term = fibonacci(n - 1)  # compute next Fibonacci term
    return previous_term + [next_term]

def main():
    number = int(input("Enter a number: "))  # user input
    print(f"The Fibonacci sequence with a length of {number} is {generate_fibonacci(number)}")  # print statement with embedded function call
    print(f"The Factorial of {number} is {math.factorial(number)}")  # function from math module called here

if __name__ == "__main__":  # will only run when executed directly
    main()