# Products of Array Except Self

## Problem Description
Given an integer array `nums`, return an array `output` where `output[i]` is the product of all the elements of `nums` except `nums[i]`.

**Constraints:**
- `2 <= nums.length <= 1000`
- `-20 <= nums[i] <= 20`
- Each product is guaranteed to fit in a 32-bit integer
- **Follow-up:** Solve it in O(n) time without using the division operation

## Solution Approach

The key insight is to use a two-pass approach that calculates the product of all elements to the left and right of each position.

### Algorithm:
1. **First Pass (Left to Right):** Calculate the product of all elements to the left of each position
2. **Second Pass (Right to Left):** Multiply each position with the product of all elements to the right

### Example Walkthrough:
For input: `[1, 2, 4, 6]`

**First Pass (Left Products):**
- Index 0: left_product = 1, output[0] = 1
- Index 1: left_product = 1*1 = 1, output[1] = 1  
- Index 2: left_product = 1*2 = 2, output[2] = 2
- Index 3: left_product = 2*4 = 8, output[3] = 8

After first pass: `output = [1, 1, 2, 8]`

**Second Pass (Right Products):**
- Index 3: right_product = 1, output[3] = 8*1 = 8
- Index 2: right_product = 1*6 = 6, output[2] = 2*6 = 12
- Index 1: right_product = 6*4 = 24, output[1] = 1*24 = 24
- Index 0: right_product = 24*2 = 48, output[0] = 1*48 = 48

Final result: `[48, 24, 12, 8]`

### Time Complexity: O(n)
- Two passes through the array, each taking O(n) time

### Space Complexity: O(1) 
- Only using a constant amount of extra space (excluding the output array)

## Key Advantages:
1. **No Division:** Avoids potential issues with zero values
2. **Optimal Time Complexity:** O(n) as required
3. **Constant Extra Space:** Only uses O(1) additional space
4. **Handles Edge Cases:** Works correctly with arrays containing zeros

## Test Cases:
- `[1, 2, 4, 6]` → `[48, 24, 12, 8]`
- `[-1, 0, 1, 2, 3]` → `[0, -6, 0, 0, 0]`
- `[1, 2, 3, 4]` → `[24, 12, 8, 6]`
- `[2, 3, 4, 5]` → `[60, 40, 30, 24]`