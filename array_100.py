# general import statements to pull in outside libraries
import random # for generating random numbers
import time # for timing the code
import matplotlib.pyplot as plt # for plotting the graph

# Generate an array of random numbers between some lower and upper limit and store them in an array called random_ints
def generate_random_number_array(lower_number_range, upper_number_range, total_number_count):
    random_ints = []
    for some_number in range (total_number_count):
        random_number = random.randint(lower_number_range, upper_number_range)
        random_ints.append(random_number)
    return random_ints

#print off the random numbers, 20 per line
def print_random_number_array(random_ints, total_number_count):
    print('printing 20 numbers per line')
    for our_number in range(total_number_count):
        print(random_ints[our_number], end = " ")
        if (our_number + 1) % 20 == 0:
            print()
    print('printing 20 numbers per line complete')


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

if __name__ == '__main__':
    # Calculate the average time taken for sorting an array of a given size
    # set up the different sizes we are going to search and soft through.
    array_sizes = [100, 500, 1000]

    # set up the number of trials we are going to run for each size
    nummber_of_trials_per_size = 5

    for size in array_sizes:
        # Generate an array of random numbers
        lower_number_range = 0
        upper_number_range = 100 * size
        random_numbers = generate_random_number_array(lower_number_range, upper_number_range, size)
        
        # Calculate the time taken for bubble_sort function
        start_time = time.time()
        for run_index in range(nummber_of_trials_per_size):
            bubble_sort(random_numbers)
            end_time = time.time()
        
            # Calculate the elapsed time
            elapsed_time = end_time - start_time
            print("Time taken for size", size, ":", elapsed_time, "seconds")

            # write data to a CSV file called bubble_sort_data.csv
            # the first time the file is created, it should add headers to the file
            # the next time the file is created, it should append to the file
            # the file should be comma separated
            # the file should be in the same directory as the code
            # the file should be opened and closed properly
            # the file should be opened in append mode
            # Headers include, run index, size of array, time taken in seconds, rounded to 3 decimal places
            
            # Write the data to a CSV file
            with open('bubble_sort_data.csv', 'a') as file:
                if run_index == 0:
                    file.write('Run Index, Size of Array, Time Taken (seconds)\n')
                file.write(str(run_index) + ',' + str(size) + ',' + str(round(elapsed_time, 3)) + '\n')



    # Read the data from the CSV file and make a new CSV file that includes
    # the best, the worst, and the average time taken for each size of array and the standard deviation of the batch
    # the file should be comma separated

    # Read the data from the CSV file
    with open('bubble_sort_data.csv', 'r') as file:
        lines = file.readlines()
        data = []
        for line in lines[1:]:
            data.append(line.strip().split(','))

    # Calculate the best, worst, average time taken for each size of array
    best_times = {}
    worst_times = {}
    average_times = {}
    standard_deviations = {}
    for size in array_sizes:
        times = []
        for line in data:
            if int(line[1]) == size:
                times.append(float(line[2]))
        best_times[size] = min(times)
        worst_times[size] = max(times)
        average_times[size] = sum(times) / len(times)
        standard_deviations[size] = (sum([(time - average_times[size]) ** 2 for time in times]) / len(times)) ** 0.5

    # Write the best, worst, average time taken for each size of array and the standard deviation of the batch to a new CSV file
    with open('bubble_sort_summary.csv', 'w') as file:
        file.write('Size of Array, Best Time (seconds), Worst Time (seconds), Average Time (seconds), Standard Deviation\n')
        for size in array_sizes:
            file.write(str(size) + ',' + str(round(best_times[size], 3)) + ',' + str(round(worst_times[size], 3)) + ',' + str(round(average_times[size], 3)) + ',' + str(round(standard_deviations[size], 3) + '\n'))



    # Create a figure with two subplots side by side
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # First subplot
    for size in array_sizes:
        times = []
        for line in data:
            if int(line[1]) == size:
                times.append(float(line[2]))
        axs[0].scatter([size] * len(times), times)
    axs[0].set_xlabel('Size of Array')
    axs[0].set_ylabel('Time Taken (seconds)')
    axs[0].set_title('Time taken for Bubble Sort')

    # Second subplot
    axs[1].scatter(list(best_times.keys()), list(best_times.values()), label='Best Time', color='red')
    axs[1].scatter(list(worst_times.keys()), list(worst_times.values()), label='Worst Time', color='blue')
    axs[1].scatter(list(average_times.keys()), list(average_times.values()), label='Average Time', color='green')
    axs[1].errorbar(list(average_times.keys()), list(average_times.values()), yerr=list(standard_deviations.values()), fmt='o', label='Standard Deviation', color='black')
    axs[1].set_xlabel('Size of Array')
    axs[1].set_ylabel('Time Taken (seconds)')
    axs[1].set_title('Time taken for Bubble Sort')
    axs[1].legend()

    # Display the figure
    plt.tight_layout()
    plt.show()

