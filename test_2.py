#BUBBLE SORT
import random

unsorted_list = [random.randint(1, 100) for _ in range(100)]

def bubble_sort(items):
    for i in range(len(items)):
        is_sorted = True
        for j in range(len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                # print(items)
                is_sorted = False

        if is_sorted:
            break
    return items



if __name__ == "__main__":
    print(bubble_sort(unsorted_list))
