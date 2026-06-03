"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

def merge_lists(a_list, b_list):
    if len(a_list) > 50 or len(b_list) > 50:
        return []
    a_list.extend(b_list)
    a_list.sort()
    if len(a_list) > 0:
        if a_list[0] < -100 or a_list[-1] > 100:
            return []
    return a_list


def main():
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]


    alist = [1, 2, 4]
    blist = [1, 3 ,4]
    print(list(merge_lists(alist, blist)))
    alist = []
    blist = []
    print(list(merge_lists(alist, blist)))
    alist = []
    blist = [0]
    print(list(merge_lists(alist, blist)))
    alist = list(range(51))
    blist = [0]
    print(list(merge_lists(alist, blist)))
    alist = list(range(3))
    blist = list(range(51))
    print(list(merge_lists(alist, blist)))
    alist = [1, 2, 100]
    blist = [1, 3 ,4]
    print(list(merge_lists(alist, blist)))
    alist = [1, 2, 1]
    blist = [1, 3 , 100]
    print(list(merge_lists(alist, blist)))
    alist = [1, 2, -100]
    blist = [1, 3 ,4]
    print(list(merge_lists(alist, blist)))
    alist = [1, 2, 4]
    blist = [1, 3 ,-100]
    print(list(merge_lists(alist, blist)))

    print(list(merge_lists(alist, blist)))
    alist = [1, 2, 101]
    blist = [1, 3 ,4]
    print(list(merge_lists(alist, blist)))
    alist = [1, 2, 1]
    blist = [1, 3 , 101]
    print(list(merge_lists(alist, blist)))
    alist = [1, 2, -101]
    blist = [1, 3 ,4]
    print(list(merge_lists(alist, blist)))
    alist = [1, 2, 4]
    blist = [1, 3 ,-101]
    print(list(merge_lists(alist, blist)))
if __name__ == "__main__":
    main()