# Code Review Notes

This document outlines identified issues in `buggy_code_examples.py`,
including logic errors, edge cases, and efficiency concerns.

---

## Function: calculate_average

**Issue Identified**
- Does not handle empty lists.
- Will raise a ZeroDivisionError when `numbers` is empty.

**Why It Matters**
- Causes runtime failure and program crashes.
- Edge cases should be handled defensively.

**Suggested Fix**
- Add a conditional check for empty input before division.

---

## Function: find_max_value

**Issue Identified**
- Initializes `max_value` to 0.
- Incorrect when all list values are negative.

**Why It Matters**
- Produces incorrect results depending on input values.

**Suggested Fix**
- Initialize `max_value` to the first element of the list.

---

## Function: remove_duplicates

**Issue Identified**
- Uses list membership checks, resulting in O(n²) time complexity.

**Why It Matters**
- Inefficient for large datasets.
- Impacts performance unnecessarily.

**Suggested Fix**
- Use a set for faster lookups.

---

## Function: count_words

**Issue Identified**
- Splitting by a single space causes inaccurate word counts.
- Multiple spaces lead to empty strings being counted.

**Why It Matters**
- Produces unreliable output for real-world text input.

**Suggested Fix**
- Use `split()` without arguments to handle variable whitespace.
