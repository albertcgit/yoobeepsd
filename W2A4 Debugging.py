def factorial(n): #BUG: Function defined as with 1 argument

    if n == 0:
        return 1
    return n * factorial(n - 1)  

def fibonacci(n): #BUG: Function defined as with 1 argument

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
    # As calls reach base cases, results pop back up and combine.

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

    #DEBUGGING: Set breakpoint here
    choice = input("Enter choice (1/2): ")

    #DEBUGGING: Step over (F8) function to go to next line until it throws an error

    # BUG: Missing number to compute for - nth series and nth factorial
    if choice == "1":
        ans = factorial() #BUG: No argument passed #DEBUGGING: Throws an error with missing 1 required positional argument
    elif choice == "2":
        ans = fibonacci() #BUG: No argument passed too
    else:
        ans = "Invalid choice"

    print("\nFinal result:", ans)