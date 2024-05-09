import random

# Function to generate a list of random numbers
def generate_random_list(length, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(length)]

# Generate a random list of numbers
length = int(input("Please enter the length of random list of numbers:"))
min_val = 1
max_val = 100
random_list = generate_random_list(length, min_val, max_val)

# function of merge sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)
# i is the initial index of first subarray, j is the second part of array, and k is the initial index of merged subarray
        i = j = k = 0

        # Merge the two sorted subarrays
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        # copy the remaining elements of R[]
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1



print("Original given list is:")
print(random_list)

# Sort the list using bubble sort
merge_sort(random_list)


print("\nSorted list using Merge Sort:")
print(random_list)
