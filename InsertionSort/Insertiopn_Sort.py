import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Function to generate a list of random numbers
def generate_random_list(length, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(length)]

# Generate a random list of numbers
length = int(input("Please enter the length of random list of numbers:"))
min_val = 1
max_val = 100
random_list = generate_random_list(length, min_val, max_val)

print("Original list:")
print(random_list)

# Sort the list using insertion sort
insertion_sort(random_list)

print("\nSorted list using Insertion Sort:")
print(random_list)
