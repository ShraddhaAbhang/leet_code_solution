'''
Question: Two Sum

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
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''


'''

To solve the problem of finding two numbers in an array that add up to a specified target, we can use a hashmap (or dictionary in Python) to efficiently store and retrieve values.

Here's the step-by-step approach using a hashmap:

Initialize a Dictionary: We'll use a dictionary to store the elements of the array as we iterate through it. The keys will be the elements themselves, and the values will be their indices.

Iterate Through the Array: As we iterate through the array, for each element nums[i], we calculate complement = target - nums[i]. This complement is the value we need to find in the array to make up the target sum.

Check if Complement Exists: Check if complement exists in the dictionary:

If it does, it means we have found the two numbers that add up to the target. Return their indices.
If it doesn't, store nums[i] in the dictionary with its index.
Edge Cases: Given the problem constraints, we can assume there is exactly one solution, so no additional checks are needed.

This approach has a time complexity of O(n), where n is the number of elements in the array. This is because accessing and inserting elements in a hashmap is average O(1) time complexity.

'''

# Solution:



