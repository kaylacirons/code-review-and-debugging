"""
Buggy Code Examples

This file contains Python functions with intentional bugs,
inefficiencies, or poor practices for review and debugging purposes.
"""

def calculate_average(numbers):
    """
    Returns the average of a list of numbers.
    """
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]

    # BUG: division by zero if list is empty
    return total / len(numbers)


def find_max_value(values):
    """
    Returns the maximum value in a list.
    """
    max_value = 0  # BUG: fails if all values are negative
    for v in values:
        if v > max_value:
            max_value = v
    return max_value


def remove_duplicates(items):
    """
    Removes duplicate items from a list.
    """
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items  # INEFFICIENT for large lists


def count_words(text):
    """
    Counts the number of words in a string.
    """
    words = text.split(" ")
    return len(words)  # BUG: extra spaces cause incorrect counts
