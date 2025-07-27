def productExceptSelf(nums):
    """
    Given an integer array nums, return an array output where output[i] is 
    the product of all the elements of nums except nums[i].
    
    Time Complexity: O(n)
    Space Complexity: O(1) excluding the output array
    """
    n = len(nums)
    output = [1] * n
    
    # Calculate products of all elements to the left of each element
    left_product = 1
    for i in range(n):
        output[i] = left_product
        left_product *= nums[i]
    
    # Multiply with products of all elements to the right of each element
    right_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]
    
    return output


# Test cases
def test_productExceptSelf():
    # Test case 1
    nums1 = [1, 2, 4, 6]
    expected1 = [48, 24, 12, 8]
    result1 = productExceptSelf(nums1)
    print(f"Test 1: {nums1}")
    print(f"Expected: {expected1}")
    print(f"Result: {result1}")
    print(f"Pass: {result1 == expected1}")
    print()
    
    # Test case 2
    nums2 = [-1, 0, 1, 2, 3]
    expected2 = [0, -6, 0, 0, 0]
    result2 = productExceptSelf(nums2)
    print(f"Test 2: {nums2}")
    print(f"Expected: {expected2}")
    print(f"Result: {result2}")
    print(f"Pass: {result2 == expected2}")
    print()
    
    # Additional test cases
    nums3 = [1, 2, 3, 4]
    expected3 = [24, 12, 8, 6]
    result3 = productExceptSelf(nums3)
    print(f"Test 3: {nums3}")
    print(f"Expected: {expected3}")
    print(f"Result: {result3}")
    print(f"Pass: {result3 == expected3}")
    print()
    
    nums4 = [2, 3, 4, 5]
    expected4 = [60, 40, 30, 24]
    result4 = productExceptSelf(nums4)
    print(f"Test 4: {nums4}")
    print(f"Expected: {expected4}")
    print(f"Result: {result4}")
    print(f"Pass: {result4 == expected4}")


if __name__ == "__main__":
    test_productExceptSelf()