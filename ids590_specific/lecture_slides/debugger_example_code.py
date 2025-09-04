"""Debugger exercise."""

from statistics import mean


def sum_numbers(list_to_sum):
    """Given a list of numbers, add up the numbers and return total"""
    total = 0
    for i in range(1, len(list_to_sum)):
        total += list_to_sum[i]
    return total


def get_mean_of_list(list_to_sum):
    """Calculate mean of numbers in a list"""
    total_of_list = sum_numbers(list_to_sum)
    number_of_numbers = len(list_to_sum)
    list_mean = total_of_list / number_of_numbers
    return list_mean


def main():
    # Test Case
    my_list = [3, 4, 5]
    print(f"The mean of {my_list} should be {mean(my_list):.2f}")

    mean_value = get_mean_of_list(my_list)

    print(f"The value from my function is is {mean_value:.2f}")


main()
