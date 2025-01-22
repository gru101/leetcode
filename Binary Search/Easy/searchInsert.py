# problem link
# https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l=0
        h=len(nums)-1

        while l<=h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                l=mid+1
            else:
                h=mid-1
        return l