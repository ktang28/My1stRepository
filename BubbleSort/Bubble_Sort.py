import random

# Function to generate a list of random numbers
def generate_random_list(length, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(length)]

# Bubble sort function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generate a random list of numbers
length = int(input("Please enter the length of random list of numbers:"))
min_val = 1
max_val = 100
random_list = generate_random_list(length, min_val, max_val)

print("Original list:")
print(random_list)

# Sort the list using bubble sort
bubble_sort(random_list)

print("\nSorted list using Bubble Sort:")
print(random_list)
