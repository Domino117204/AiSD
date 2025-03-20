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

def quick_sort_left_pivot(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [x for x in data[1:] if x <= pivot]
    right = [x for x in data[1:] if x > pivot]
    return quick_sort_left_pivot(left) + [pivot] + quick_sort_left_pivot(right)

def quick_sort_random_pivot(data):
    if len(data) <= 1:
        return data
    pivot_index = random.randint(0, len(data) - 1)
    pivot = data[pivot_index]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort_random_pivot(left) + middle + quick_sort_random_pivot(right)

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
ilosc = input("Podaj n - ilość elementów w tablicy (potęga 2 od 4 do 32768)\n")
missing_zeros = 8 - len(ilosc)
zeros = missing_zeros*"0"
filename = "/mnt/c/users/oliwe/AiSD/AiSD/benchmark/"+typ_tabeli+"_"+zeros+ilosc+".txt"
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
