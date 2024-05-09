def fibonacci(num):
    a=0
    b=1
    fibonacci_series=[]

    while len(fibonacci_series)<num:
     fibonacci_series.append(a)
     a,b = b, a+b
    return fibonacci_series

number = int(input("Please enter the number of fibonacciseries:"))
fib_series = fibonacci(number)
print(fib_series)
