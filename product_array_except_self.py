"""
Products of Array Except Self

Given an integer array nums, return an array output where output[i] is the product of all the
elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Optimal O(n) time, O(1) extra space solution (not counting output array).
        
        Approach:
        1. First pass: Calculate left products for each position
        2. Second pass: Calculate right products on the fly and multiply with left products
        
        Time Complexity: O(n)
        Space Complexity: O(1) extra space
        """
        n = len(nums)
        result = [1] * n
        
        # First pass: calculate left products
        # result[i] will contain product of all elements to the left of nums[i]
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]
        
        # Second pass: calculate right products and multiply with left products
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result
    
    def productExceptSelf_twoArrays(self, nums: List[int]) -> List[int]:
        """
        Alternative approach using two separate arrays for left and right products.
        
        Time Complexity: O(n)
        Space Complexity: O(n) extra space
        """
        n = len(nums)
        left = [1] * n
        right = [1] * n
        result = [1] * n
        
        # Calculate left products
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        
        # Calculate right products
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        # Multiply left and right products
        for i in range(n):
            result[i] = left[i] * right[i]
        
        return result
    
    def productExceptSelf_withDivision(self, nums: List[int]) -> List[int]:
        """
        Solution using division (not allowed in follow-up, but good to understand).
        
        Note: This approach has edge cases with zeros that need special handling.
        
        Time Complexity: O(n)
        Space Complexity: O(1) extra space
        """
        n = len(nums)
        total_product = 1
        zero_count = 0
        zero_index = -1
        
        # Calculate total product and count zeros
        for i, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                zero_index = i
            else:
                total_product *= num
        
        result = [0] * n
        
        if zero_count > 1:
            # If more than one zero, all products are zero
            return result
        elif zero_count == 1:
            # If exactly one zero, only that position has non-zero product
            result[zero_index] = total_product
        else:
            # No zeros, divide total product by each element
            for i in range(n):
                result[i] = total_product // nums[i]
        
        return result


def test_solution():
    """Test the solution with provided examples."""
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 4, 6]
    expected1 = [48, 24, 12, 8]
    result1 = solution.productExceptSelf(nums1)
    print(f"Test 1:")
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: {expected1}")
    print(f"Correct: {result1 == expected1}")
    print()
    
    # Test case 2
    nums2 = [-1, 0, 1, 2, 3]
    expected2 = [0, -6, 0, 0, 0]
    result2 = solution.productExceptSelf(nums2)
    print(f"Test 2:")
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: {expected2}")
    print(f"Correct: {result2 == expected2}")
    print()
    
    # Additional test cases
    # Edge case: array with two elements
    nums3 = [2, 3]
    expected3 = [3, 2]
    result3 = solution.productExceptSelf(nums3)
    print(f"Test 3 (Edge case - two elements):")
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: {expected3}")
    print(f"Correct: {result3 == expected3}")
    print()
    
    # Edge case: array with negative numbers
    nums4 = [-2, -3, 4]
    expected4 = [-12, -8, 6]
    result4 = solution.productExceptSelf(nums4)
    print(f"Test 4 (Negative numbers):")
    print(f"Input: {nums4}")
    print(f"Output: {result4}")
    print(f"Expected: {expected4}")
    print(f"Correct: {result4 == expected4}")


if __name__ == "__main__":
    test_solution()