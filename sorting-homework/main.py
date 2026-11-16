import random
import time
import matplotlib.pyplot as plt


def bubble_sort(items):
    result = items.copy()

    for i in range(len(result)):
        for j in range(0, len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


def selection_sort(items):
    result = items.copy()

    for i in range(len(result)):
        min_index = i

        for j in range(i + 1, len(result)):
            if result[j] < result[min_index]:
                min_index = j

        result[i], result[min_index] = result[min_index], result[i]

    return result


def insertion_sort(items):
    result = items.copy()

    for i in range(1, len(result)):
        current = result[i]
        j = i - 1

        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = current

    return result


numbers = [8, 3, 5, 1, 9, 2, 7, 4, 6]

print("Original list:", numbers)
print("Bubble sort:", bubble_sort(numbers))
print("Selection sort:", selection_sort(numbers))
print("Insertion sort:", insertion_sort(numbers))


sizes = [100, 500, 1000, 2000]

bubble_times = []
selection_times = []
insertion_times = []

repeats = 3

for size in sizes:
    data = [random.randint(1, 10000) for _ in range(size)]

    start = time.perf_counter()
    for _ in range(repeats):
        bubble_sort(data)
    bubble_times.append((time.perf_counter() - start) / repeats)

    start = time.perf_counter()
    for _ in range(repeats):
        selection_sort(data)
    selection_times.append((time.perf_counter() - start) / repeats)

    start = time.perf_counter()
    for _ in range(repeats):
        insertion_sort(data)
    insertion_times.append((time.perf_counter() - start) / repeats)


print("\nExecution time comparison:")

for i in range(len(sizes)):
    print("List size:", sizes[i])
    print("Bubble sort:", bubble_times[i], "seconds")
    print("Selection sort:", selection_times[i], "seconds")
    print("Insertion sort:", insertion_times[i], "seconds")
    print()


plt.plot(sizes, bubble_times, marker="o", label="Bubble sort")
plt.plot(sizes, selection_times, marker="o", label="Selection sort")
plt.plot(sizes, insertion_times, marker="o", label="Insertion sort")

plt.xlabel("List size")
plt.ylabel("Execution time (seconds)")
plt.title("Sorting Algorithms Comparison")
plt.legend()
plt.grid(True)

plt.savefig("sorting_comparison.png")
plt.show()