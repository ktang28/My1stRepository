def fibonacciRecur(n):
    # Base cases: fibonacci(0) = 0, fibonacci(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    else:
        return fibonacciRecur(n-1) + fibonacciRecur(n-2)


def display_Fiboncci_Series(n):
   if n<0:
       print("Please enter a positive number:")
   else:
       print("Fibonacci series up to", n, ":")
       for i in range(n):
           print(fibonacciRecur(i), end=" ")


# Example usage:
number = int(input("Please enter a number:"))
result = display_Fiboncci_Series(number)
print(result)
