'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        s = set(nums)
        for val in range(1, n+1):
            if val not in s:
                res.append(val)
            
        return res

### Method 2
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        all_nums = [0] * n

        # placing all values from nums to all_nums arr(0 based indexing)
        for val in nums:
            all_nums[val-1] = val

        res = []
        # whichever index val is zero -> index + 1 is missing number in that range
        for idx in range(n):
            if all_nums[idx] == 0:
                res.append(idx+1)
        
        return res
