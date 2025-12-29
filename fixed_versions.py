"""
Fixed Versions of Buggy Code Examples

Each function below addresses logic, efficiency,
and clarity issues identified during code review.
"""

def calculate_average(numbers):
    """
    Returns the average of a list of numbers.
    Safely handles empty lists.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def find_max_value(values):
    """
    Returns the maximum value in a list.
    """
    if not values:
        return None

    max_value = values[0]
    for v in values:
        if v > max_value:
            max_value = v
    return max_value


def remove_duplicates(items):
    """
    Removes duplicate items while preserving order.
    """
    seen = set()
    unique_items = []

    for item in items:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)

    return unique_items


def count_words(text):
    """
    Counts the number of words in a string accurately.
    """
    words = text.split()
    return len(words)
