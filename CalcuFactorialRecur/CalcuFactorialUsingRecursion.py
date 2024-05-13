def cal_Factorial_Recur(n):
    if n == 0:
        return 1
    else:
        return n * cal_Factorial_Recur (n-1)

number = int(input("Please enter a numner:"))
result = cal_Factorial_Recur(number)
print("Factorial of", number, "is:", result)

