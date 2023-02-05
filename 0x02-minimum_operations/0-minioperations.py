#!/usr/bin/pytho#!/usr/bin/python3
""" 0-minoperations module """


def minOperations(n):
    """
    method that calculates the fewest number of operations needed to result in
    exactly n H characters in the file with a single character H. Only two
    operations can be executed in this file: Copy All and Paste
    """
    pasted_chars = 1  # no of chars in file
    clipboard = 0  # no of H's copied
    counter = 0  # operations counter

    while pasted_chars < n:
        if clipboard == 0:  # if nothing is copied
            clipboard = pasted_chars  # copy all
            counter += 1  # increment operations counter

        if pasted_chars == 1:  # if nothing is pasted
            pasted_chars += clipboard  # paste
            counter += 1  # increment operations counter
            continue  # continue to the next loop

        remaining = n - pasted_chars  # no of remaining chars to paste

        """
        if no of chars to be pasted is more than remaing no of chars,
        operation is aborted
        """
        if remaining < clipboard:
            return 0

        # if remaining chars are not divisible by no of chars to be pasted
        if remaining % pasted_chars != 0:
            pasted_chars += clipboard  # paste current clipboard
            counter += 1  # increment operations counter
        else:
            clipboard = pasted_chars  # copy all
            pasted_chars += clipboard  # paste
            counter += 2  # increment operations counter

    if pasted_chars == n:  # if got the desired result
        return counter
    else:
        return 0
