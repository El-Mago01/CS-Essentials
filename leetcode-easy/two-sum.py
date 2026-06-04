"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""
# Input: nums = [2,7,11,15], target = 9
def two_sum(nums, target):
    answer = []
    for index in range(len(nums)): #range(4)
        search_item = target - nums[index] #search_item = 9 -2 =7
        if search_item in nums:
            found_index = nums.index(search_item)
            answer.append(index)
            answer.append(found_index)
            return answer
    return answer


def main():
    input_array = [2,7,11,15]
    target = 9
    ranger = range(len(input_array))
    print("ranger", ranger)
    for i in ranger:
        print(i)
    print(two_sum(input_array, target))


if __name__ == "__main__":
    main()