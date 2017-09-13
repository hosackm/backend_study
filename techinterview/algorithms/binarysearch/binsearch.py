import random


def _binary_search_recursive(arr, x):
    # base case, we've only got one element left
    if len(arr) == 1:
        return arr[0] == x

    # check the middle for a match otherwise recurse on the left half or right half
    mid = len(arr) // 2
    if x == arr[mid]:
        return True
    elif x > arr[mid]:
        return _binary_search_recursive(arr[mid:], x)
    else:
        return _binary_search_recursive(arr[:mid], x)


def binary_search(arr, x, key=lambda x: x):
    """
    Find an element x in a list arr.  You may pass a key to use to sort the array.
    """
    # call recursive binary search helper function
    return _binary_search_recursive(sorted(arr), x)

if __name__ == "__main__":
    x = 42
    if binary_search([random.randint(1, 100) for _ in range(100000)], x):
        print(x, "is in the list!")
