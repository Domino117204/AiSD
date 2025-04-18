import sys
import random
import time

sys.setrecursionlimit(10**6)

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def sedgewick_gaps(n):
    gaps = []
    k = 0
    while True:
        if k % 2 == 0:
            gap = 9 * (2 ** k) - 9 * (2 ** (k // 2)) + 1
        else:
            gap = 4 ** k + 3 * 2 ** (k - 1) + 1
        
        if gap >= n:
            break
        gaps.append(gap)
        k += 1

    return gaps[::-1]
# zoptymalizować tak żeby nie tworzyć listy gaps, tylko wgrać maksymalny gap do funkcji i później k zmniejszać o 1

def shell_sort(data):
    n = len(data)
    gaps = sedgewick_gaps(n)
    
    for gap in gaps:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
    return data
# zamiast używać temp to użyć funkcji swap, dzięki czemu nie potrzeba dodatkowej zmiennej do przechowywania 

def selection_sort(data):
    n = len(data)
    for j in range(n - 1):
        min_idx = j
        for i in range(j + 1, n):
            if data[i] < data[min_idx]:
                min_idx = i
        data[j], data[min_idx] = data[min_idx], data[j]
    return data

def heap(data, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left
    if right < n and data[right] > data[largest]:
        largest = right
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heap(data, n, largest)

def heap_sort(data):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heap(data, n, i)
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heap(data, i, 0)
    return data

def partition(A, p, r):
    pivot = A[p]
    i = p+1
    j = r

    while True:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] > pivot:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
        else:
            break

    A[p], A[j] = A[j], A[p]
    return j

def quick_sort_left_pivot(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort_left_pivot(A, p, q-1)
        quick_sort_left_pivot(A, q+1, r)
    return A

def quick_sort_random_pivot(data):
    if len(data) <= 1:
        return data
    
    pivot_index = random.randint(0, len(data) - 1)
    pivot = data[pivot_index]
    
    left = []
    middle = []
    right = []
    
    for i, x in enumerate(data):
        if i == pivot_index:
            middle.append(x)
        elif x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
    
    return quick_sort_random_pivot(left) + middle + quick_sort_random_pivot(right)

#def quick_sort(array, pivot_f):
#    pivot = pivot_f(array)
#    ...

#def quick_sort_left(array):
#    def left_pivot(array):
#        return array[0]
#    quick_sort(array, left_pivot)
#
#    quick_sort(array, lambda array : array [0] )

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
        return quick_sort_left_pivot(data, 0, len(data) - 1)
    elif algorithm == 6:
        return quick_sort_random_pivot(data)
    else:
        print("Błąd: Niepoprawny numer algorytmu.")
        return None

def read_data_from_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            size = int(lines[0].strip())  # Pierwsza linia to liczba elementów
            data = [int(line.strip()) for line in lines[1:size+1]]  # Wczytaj `size` elementów
            return data
    except FileNotFoundError:
        print(f"Błąd: Plik '{filename}' nie istnieje.")
        return None
    except ValueError:
        print(f"Błąd: Plik '{filename}' zawiera niepoprawne dane.")
        return None

#filename = input("Podaj nazwę pliku z danymi: ")
typ_tabeli = input("Podaj typ tabeli do posortowania: a_shaped_array, constant_array, decreasing_array, increasing_array, random_array\n")
ilosc = input("Podaj n - ilość elementów w tablicy (potęga 2 od 4 do 65536)\n")
missing_zeros = 8 - len(str(ilosc))
zeros = missing_zeros * "0"
filename = "benchmark/" + typ_tabeli + "_" + zeros + str(ilosc) + ".txt"
data = read_data_from_file(filename)

if data is not None:
    algorithm = int(input("Podaj numer algorytmu: \n 1 - Insertion Sort \n 2 - Shell Sort \n 3 - Selection Sort \n 4 - Heap Sort \n 5 - Quick Sort (Left Pivot) \n 6 - Quick Sort (Random Pivot)\n"))
    start = time.time()
    sorted_data = sort_using_algorithm(data.copy(), algorithm)
    end = time.time()
    algorithm_time = end-start

    if sorted_data is not None:
        print("Dane przed sortowaniem:", data)
        print()
        print("Posortowane dane:", sorted_data)
        print()
        print("Czas wykonania: ", algorithm_time, "sekund")
