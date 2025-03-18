import sys

def insertion_sort (data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def shell_sort(data):
    n=len(data)
    gap = n//2
    while gap>0:
        for i in range(gap, n):
            temp=data[i]
            j=i
            while j>=gap and data[j-gap]> temp:
                data[j]=data[j-gap]
                j-=gap
            data[j]=temp
        gap//=2
    return data
 
def selection_sort(data):
    n=len(data)
    for j in range(n-1):
        min = j
        for i in range(j+1, n):
            if data[i] < data[min]:
                min = i
        data[j], data[min] = data[min], data[j]
    return data

def heap(data,n,i):
    largest=i
    left = 2*i+1
    right = 2*i+2

    if left<n and data[left]>data[largest]:
        largest = left
    if right<n and data[right]>data[largest]:
        largest=right
    if largest !=i:
        data[i], data[largest]=data[largest],data[i]
        heap(data, n, largest)

def heap_sort(data):
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):  
        heap(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heap(data, i, 0)

    return data

def quick_sort_left_pivot(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [x for x in data[1:] if x <= pivot]
    right = [x for x in data[1:] if x > pivot]
    return quick_sort_left_pivot(left) + [pivot] + quick_sort_left_pivot(right)

#def quick_sort_random_pivot():

def sort_using_algorithm(data, algorithm):
    if algorithm == 1:
        return insertion_sort(data)
    elif algorithm == 2:
        return shell_sort(data)
    elif algorithm == 3:
        return selection_sort(data)
    elif algorithm == 4:
        return heap_sort(data)
    elif algorithm == 5:
        return quick_sort_left_pivot(data)
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
