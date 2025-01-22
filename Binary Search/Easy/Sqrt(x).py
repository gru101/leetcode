# problem link
# https://leetcode.com/problems/sqrtx/

"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""



class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 1, x

        while l <= h:
            mid = (l + h) // 2
            ms = mid ** 2

            if ms == x:
                return mid

            if ms > x:
                h = mid - 1
            else:
                l = mid + 1

        return h
