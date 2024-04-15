# Generate an array of 100 random floating-point numbers between -10 and 10
upper_number_range = 10
lower_number_range = -10
random_floats = []
total_number_count = 100
for some_number in range (total_number_count):
    random_number = random.uniform(lower_number_range, upper_number_range)
    random_floats.append(random_number)

#print off the random numbers, 20 per line
for our_number in range(total_number_count):
    print(random_floats[our_number], end = " ")
    if (our_number + 1) % 20 == 0:
        print()

print(random_floats)
def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the array
    for i in range(n):
        # Flag to optimize if already sorted
        swapped = False
        
        # Last i elements are already in place, no need to traverse them again
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
                swapped = True
        
        # If no two elements were swapped, the array is already sorted
        if not swapped:
            break

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)
import random

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the array
    for i in range(n):
        # Flag to optimize if already sorted
        swapped = False
        
        # Last i elements are already in place, no need to traverse them again
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
                swapped = True
        
        # If no two elements were swapped, the array is already sorted
        if not swapped:
            break

# Generate an array of 100 random numbers
random_numbers = [random.randint(1, 1000) for _ in range(100)]

# Test the bubble_sort function with the array of random numbers
bubble_sort(random_numbers)

# Print the sorted array
print("Sorted array:", random_numbers)
import random
import time

def bubble_sort(arr):
    n = len(arr)
    
    # Start the timer
    start_time = time.time()
    
    # Traverse through all elements in the array
    for i in range(n):
        # Flag to optimize if already sorted
        swapped = False
        
        # Last i elements are already in place, no need to traverse them again
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
                swapped = True
        
        # If no two elements were swapped, the array is already sorted
        if not swapped:
            break
    
    # Stop the timer
    end_time = time.time()
    
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    print("Time taken for sorting:", elapsed_time, "seconds")

# Generate an array of 100 random numbers
random_numbers = [random.randint(1, 1000) for _ in range(100)]

# Test the bubble_sort function with the array of random numbers
bubble_sort(random_numbers)

# Print the sorted array
print("Sorted array:", random_numbers)
import random
import time
import csv

def bubble_sort(arr):
    n = len(arr)
    
    # Start the timer
    start_time = time.time()
    
    # Traverse through all elements in the array
    for i in range(n):
        # Flag to optimize if already sorted
        swapped = False
        
        # Last i elements are already in place, no need to traverse them again
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
                swapped = True
        
        # If no two elements were swapped, the array is already sorted
        if not swapped:
            break
    
    # Stop the timer
    end_time = time.time()
    
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    
    return elapsed_time

# Generate an array of 100 random numbers
random_numbers = [random.randint(1, 1000) for _ in range(100)]

# Perform
import time

# Record the start time
start_time = time.time()

# Your code to be timed goes here
# For example, a bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print("Time taken:", elapsed_time, "seconds")
import time
import random

# Record the start time
start_time = time.time()

# Your code to be timed goes here
# For example, a bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generate an array of 1000 random numbers
arr = [random.randint(1, 1000) for _ in range(1000)]

# Sort the array using bubble sort
bubble_sort(arr)

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print("Time taken:", elapsed_time, "seconds")
import time
import random

# Record the start time
start_time = time.time()

# Your code to be timed goes here
# For example, a bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generate an array of 10,000 random numbers
arr = [random.randint(1, 10000) for _ in range(10000)]

# Sort the array using bubble sort
bubble_sort(arr)

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print("Time taken:", elapsed_time, "seconds")
import time
import random

# Record the start time
start_time = time.time()

# Your code to be timed goes here
# For example, a bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generate an array of 100,000 random numbers
arr = [random.randint(1, 100000) for _ in range(100000)]

# Sort the array using bubble sort
bubble_sort(arr)

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print("Time taken:", elapsed_time, "seconds")
import time
import random

# Record the start time
start_time = time.time()

# Your code to be timed goes here
# For example, a bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generate an array of one million random numbers
arr = [random.randint(1, 1000000) for _ in range(1000000)]

# Sort the array using bubble sort
bubble_sort(arr)

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print("Time taken:", elapsed_time, "seconds")
import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Function to calculate average time for sorting
def calculate_average_time(array_sizes, num_trials):
    average_times = []
    for size in array_sizes:
        total_time = 0
        for _ in range(num_trials):
            arr = [random.randint(1, 1000) for _ in range(size)]
            start_time = time.time()
            bubble_sort(arr)
            end_time = time.time()
            total_time += end_time - start_time
        average_time = total_time / num_trials
        average_times.append(average_time)
    return average_times

# Array sizes to test
array_sizes = [100, 500, 1000, 5000, 10000]
num_trials = 5

# Calculate average times
average_times = calculate_average_time(array_sizes, num_trials)

# Plotting the graph
plt.plot(array_sizes, average_times, marker='o')
plt.title('Time vs Size for Bubble Sort')
plt.xlabel('Size of Array')
plt.ylabel('Average Time (seconds)')
plt.grid(True)
plt.show()
