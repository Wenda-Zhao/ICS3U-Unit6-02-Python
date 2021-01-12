#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Jan 2021
# This program for list


def max_number(my_numbers):
    # This function is for calculate

    basic_number = 0

    # process
    for loop_number in range(0, len(my_numbers)):
        if my_numbers[loop_number] >= basic_number:
            basic_number = my_numbers[loop_number]

    return basic_number


def main():
    # This function is for list

    import random
    my_numbers = []

    # process
    for loop_number in range(0, 10):
        some_variable = random.randint(0, 10)
        my_numbers.append(some_variable)
        # call function
        largest_number = max_number(my_numbers)
    for loop_number in range(0, 10):
        print("The number is: {0}".format(my_numbers[loop_number]))
    print("")
    print("The largest number is: {0}".format(largest_number))


if __name__ == "__main__":
    main()
