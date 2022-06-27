import matplotlib.pyplot as plt
import numpy as np
import random

amount = 20
lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

choice = input("Type B for Bubble Sort and M for Merge Sort: ")

if choice == 'B':
    # bubble sort
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            plt.bar(x, lst, )
            plt.pause(0.001)
            plt.clf()
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    plt.show()

if choice == 'M':
    # merge sort
    random.seed('ABC')
    numbers = [random.randint(0, 1000) for _ in range(amount)]


    def merge_sort(number_list, left, right):
        # base case
        if left >= right:
            return

        # find the middle
        mid = (left + right) // 2

        plt.bar(list(range(amount)), number_list)
        plt.pause(0.01)
        plt.clf()

        # split recursively into left and right halves
        merge_sort(number_list, left, mid)
        merge_sort(number_list, mid + 1, right)

        # plt.bar(list(range(amount)), number_list)
        # plt.pause(0.01)
        # plt.clf()

        # merge the two results
        def merge(number_list, left, right, mid):
            left_cpy = number_list[left:mid + 1]
            right_cpy = number_list[mid + 1: right + 1]

            l_counter, r_counter = 0, 0
            sorted_counter = left

            while l_counter < len(left_cpy) and r_counter < len(right_cpy):
                if left_cpy[l_counter] <= right_cpy[r_counter]:
                    number_list[sorted_counter] = left_cpy[l_counter]
                    l_counter += 1
                else:
                    number_list[sorted_counter] = right_cpy[r_counter]
                    r_counter += 1

                sorted_counter += 1

            while l_counter < len(left_cpy):
                number_list[sorted_counter] = left_cpy[l_counter]
                l_counter += 1
                sorted_counter += 1

            while r_counter < len(right_cpy):
                number_list[sorted_counter] = right_cpy[r_counter]
                r_counter += 1
                sorted_counter += 1

        merge(number_list, left, right, mid)

        plt.bar(list(range(amount)), number_list)
        plt.pause(0.01)
        plt.clf()


    merge_sort(numbers, 0, len(numbers) - 1)
    print(numbers)
    plt.bar(list(range(amount)), numbers)
    plt.show()

else:
    print("Incorrect input")
