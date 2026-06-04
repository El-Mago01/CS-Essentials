def binary_search_rec(lst, target):
    return binary_search_helper(lst, target, 0, len(lst))


def binary_search_helper(lst, target, left, right):
    print(f"binary_search_helper({lst},{target},{left},{right}")
    if left > right:
        return None
    mid = (left + right) // 2

    if lst[mid] == target:
        return mid

    if lst[mid] > target:
        return binary_search_helper(lst, target, left, mid-1)
    else:
        return binary_search_helper(lst, target, mid+1, right)

print("Searching in [1, 5, 11, 16, 23]")
print(f"5 is at: {binary_search_rec([1, 5, 11, 16, 23], 5)}")
print(f"3 is at: {binary_search_rec([1, 5, 11, 16, 23], 3)}")
