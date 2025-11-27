import math

def generate_fibonacci(length): #my function for generating fibonacci series

    if length < 0: #negative value as length is invalid
        return "invalid"
    elif length == 0: #0 as length is empty series
        return []
    elif length == 1:#1 as length is [0]
        return [0]
    else: #valid length
        fibonacci_series = [0, 1] #Setting base values for F(0) and F(1)
        for n in range(2,length): #Loop to get next values until F(length-1) and return
            next_term = fibonacci_series[n-1] + fibonacci_series[n-2]
            fibonacci_series.append(next_term)
        return fibonacci_series

def main():
    number = int(input("Enter a number: ")) #user input
    print(f"The Fibonacci sequence with a length of {number} is {generate_fibonacci(number)}") #print statement with embedded function call
    print(f"The Factorial of {number} is {math.factorial(number)}") #function from math module called here

if __name__ == "__main__": #will only run when executed directly
    main()