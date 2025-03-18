import sys
# test2
def insertion_sort (data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data
#abce
#def shell_sort():
#    
#def selection_sort():
#
#def heap_sort():
#
#def quick_sort_left_pivot():
#
#def quick_sort_random_pivot():

def sort_using_algorithm(data, algorithm):
    if algorithm == 1:
        return insertion_sort(data)
    #elif algorithm == 2:
    #    return shell_sort(data)
    #elif algorithm == 3:
    #    return selection_sort(data)
    #elif algorithm == 4:
    #    return heap_sort(data)
    #elif algorithm == 5:
    #    return quick_sort_left_pivot(data)
    #elif algorithm == 6:
    #    return quick_sort_random_pivot(data)

def main():
    # Command-line arguments: python script.py --algorithm <algorithm_number>
    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>")
        sys.exit(1)

    algorithm_number = int(sys.argv[2])

    # Read input data from standard input until the end of file (EOF)
    input=sys.stdin.read().split()
    try:
        data = [int(x) for x in input[1:]]
    except EOFError:
        print("Error reading input.")

    # Perform sorting using the specified algorithm (ignored in this example)
    sorted_data = sort_using_algorithm(data, algorithm_number)

    # Print the sorted data
    print("Sorted data:", sorted_data[0:10])

if __name__ == "__main__":
    main()
