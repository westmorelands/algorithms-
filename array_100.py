"""
This code is to explore how the bubble sort algorithm works
and how it takes more time to run the bigger the problem it works on.
It should do a few runs for each size of array.
It should keep track of how many numbers were sorted
And it should store how long it took to complete the task.

The code should then turn around and create a CSV file with the data
The CSV file should have the following columns:
- Run Index
- Size of Array
- Time Taken (seconds)

The code should then read the data from the CSV file and make a new CSV file that includes
the best, the worst, and the average time taken for each size of array and the standard deviation of the batch
The file should be comma separated

"""

# general import statements to pull in outside libraries
import random # for generating random numbers
import time # for timing the code


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
    for outer_loop_index in range(n):
        # Flag to optimize if already sorted
        swapped = False
        
        # Last i elements are already in place, no need to traverse them again
        for inner_loop_single_pass_index in range(0, n-outer_loop_index-1):
            # Swap if the element found is greater than the next element
            if arr[inner_loop_single_pass_index] > arr[inner_loop_single_pass_index+1]:
                arr[inner_loop_single_pass_index], arr[inner_loop_single_pass_index+1] = arr[inner_loop_single_pass_index+1], arr[inner_loop_single_pass_index]  # Swap
                swapped = True
        
        # If no two elements were swapped, the array is already sorted
        if not swapped:
            break

if __name__ == '__main__':
    # Calculate the average time taken for sorting an array of a given size
    # set up the different sizes we are going to search and soft through.
    array_sizes = [10, 25, 50]

    # set up the number of trials we are going to run for each size
    nummber_of_trials_per_size = 3

    # create a dictionary to store the data. the key will be the size of the array for the first dictionary.
    # the value of the first dictionary will be another dictionary with the following key value pairs:
    # trial number with a value of the time taken to sort the array

    data_dict = {}
    for size in array_sizes:
        data_dict[size] = {}
        for trial_number in range(nummber_of_trials_per_size):
            data_dict[size][trial_number] = 0

    for size in array_sizes:
        # Generate an array of random numbers
        lower_number_range = 0
        upper_number_range = 100 * size
        

        # Calculate the time taken for bubble_sort function
        
        for run_index in range(nummber_of_trials_per_size):
            random_numbers = generate_random_number_array(lower_number_range, upper_number_range, size)
        
            print_random_number_array(random_numbers, size)

            start_time = time.time()
            bubble_sort(random_numbers)
            end_time = time.time()
        
            # Calculate the elapsed time
            elapsed_time = end_time - start_time
            print("Time taken for size", size, ":", elapsed_time, "seconds")
            data_dict[size][run_index] = elapsed_time

            # write data to a CSV file called bubble_sort_data.csv
            # the first time the file is created, it should add headers to the file
            # the next time the file is created, it should append to the file
            # the file should be comma separated
            # the file should be in the same directory as the code
            # the file should be opened and closed properly
            # the file should be opened in append mode
            # Headers include, run index, size of array, time taken in seconds, rounded to 3 decimal places
            
            print('writing raw data to a CSV file')
            # Write the data to a CSV file
            with open('bubble_sort_data.csv', 'a') as file:
                if run_index == 0:
                    file.write('Run Index, Size of Array, Time Taken (seconds)\n')
                file.write(str(run_index) + ',' + str(size) + ',' + str(round(elapsed_time, 3)) + '\n')

   

    # use the data dictionary.
    # work through each size of array and calculate the best, worst, average, and standard deviation of the time taken
    # write this to a new data dictionary called summary_data_dict

    summary_data_dict = {}
    for size in array_sizes:
        summary_data_dict[size] = {}
        summary_data_dict[size]['best'] = min(data_dict[size].values())
        summary_data_dict[size]['worst'] = max(data_dict[size].values())
        summary_data_dict[size]['average'] = sum(data_dict[size].values()) / nummber_of_trials_per_size
        summary_data_dict[size]['standard_deviation'] = 0

        # Calculate the standard deviation
        for trial_number in range(nummber_of_trials_per_size):
            summary_data_dict[size]['standard_deviation'] += (data_dict[size][trial_number] - summary_data_dict[size]['average']) ** 2
        summary_data_dict[size]['standard_deviation'] = (summary_data_dict[size]['standard_deviation'] / nummber_of_trials_per_size) ** 0.5

    
    print('start graphing the summary data')

 
    # make a plot with two subplots.  
    # the first subplot should be a scatter plot of the raw data.
    # the x-axis should be the size of the array
    # the y-axis should be the time taken to sort the array

    # the second subplot should be a whisker plot of the summary data
    # the x-axis should be the size of the array
    # the y-axis should be the best, worst, average, and standard deviation of the time taken to sort the array

    # the plot should be saved as a PNG file called bubble_sort_summary.png

    import matplotlib.pyplot as plt # type: ignore
    
