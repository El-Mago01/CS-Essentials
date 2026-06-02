"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

When the list is empty, return "ERROR" as a string
if the input is not a list, escalate to TypeError with explanation how to fix
"""

def running_sum(nums :list):
    answer = []
    if len(nums) == 0 or type(nums) != list:
        raise TypeError(f"You provided the wrong type. You provided a {type(nums)} where it should have been a list")
    if not(1 <= len(nums) <= 1000):
        return "ERROR"
    for index in range(len(nums)):
        if not (-1000000 <= nums[index] <= 1000000):
            return "ERROR"
        if index == 0:
            answer.append(nums[index])
        else:
            answer.append(answer[index-1] + nums[index])
    return answer

def main():
    my_list = []
    for i in range(1000):
        my_list.append(i)
    print(running_sum(my_list))
    my_list.append(1001)
    print(running_sum(my_list))
    my_list = [-1000000, 1000000]
    print(running_sum(my_list))
    my_list = [-1000001, 1000000]
    print(running_sum(my_list))
    my_list = [-1000000, 1000001]
    print(running_sum(my_list))
    my_list = [1,2,3,4]
    print(running_sum(my_list))
    my_list = [1, 1, 1, 1, 1]
    print(running_sum(my_list))
    my_list = [3, 1, 2, 10, 1]
    print(running_sum(my_list))

    # my_list = []
    # print(running_sum(my_list))
    my_list = {}
    print(running_sum(my_list))


if __name__ == "__main__":
    main()