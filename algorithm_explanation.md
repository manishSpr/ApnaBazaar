# Products of Array Except Self - Algorithm Explanation

## Problem Statement
Given an integer array `nums`, return an array `output` where `output[i]` is the product of all the elements of `nums` except `nums[i]`.

**Constraints:**
- Each product is guaranteed to fit in a 32-bit integer
- Follow-up: Solve it in O(n) time without using division

## Solution Approaches

### 1. Optimal Solution - O(n) Time, O(1) Extra Space

This is the **recommended approach** that solves the follow-up challenge.

**Key Insight:** For each position `i`, we need:
- Product of all elements to the left of `i`
- Product of all elements to the right of `i`
- Final result = left_product × right_product

**Algorithm:**
1. **First Pass (Left to Right):** Calculate left products
   - `result[i]` = product of all elements to the left of `nums[i]`
2. **Second Pass (Right to Left):** Calculate right products on-the-fly
   - Multiply `result[i]` with the running right product

**Example Walkthrough:**
```
Input: [1, 2, 4, 6]

Step 1 - Left products:
result = [1, 1, 2, 8]
         ↑  ↑  ↑  ↑
         1  1  1×2  1×2×4

Step 2 - Right products (calculated on-the-fly):
right_product starts at 1, goes from right to left

i=3: result[3] = 8 × 1 = 8,     right_product = 1 × 6 = 6
i=2: result[2] = 2 × 6 = 12,    right_product = 6 × 4 = 24
i=1: result[1] = 1 × 24 = 24,   right_product = 24 × 2 = 48
i=0: result[0] = 1 × 48 = 48,   right_product = 48 × 1 = 48

Final result: [48, 24, 12, 8]
```

**Time Complexity:** O(n) - Two passes through the array
**Space Complexity:** O(1) - Only using the output array and a single variable

### 2. Two Arrays Approach - O(n) Time, O(n) Extra Space

This approach is easier to understand but uses more space.

**Algorithm:**
1. Create `left[]` array where `left[i]` = product of elements to the left of `i`
2. Create `right[]` array where `right[i]` = product of elements to the right of `i`
3. For each `i`, `result[i] = left[i] × right[i]`

### 3. Division Approach (Not Allowed in Follow-up)

**Algorithm:**
1. Calculate total product of all elements
2. For each position `i`, `result[i] = total_product / nums[i]`

**Edge Cases with Division:**
- **Zero elements:** Need special handling
- **Multiple zeros:** All results are zero
- **Single zero:** Only the zero position gets non-zero result

## Code Implementation

The main solution uses the optimal O(1) space approach:

```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n
    
    # First pass: calculate left products
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]
    
    # Second pass: calculate right products and multiply
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result
```

## Test Cases Verification

✅ **Test 1:** `[1, 2, 4, 6]` → `[48, 24, 12, 8]`
✅ **Test 2:** `[-1, 0, 1, 2, 3]` → `[0, -6, 0, 0, 0]`
✅ **Edge Case:** `[2, 3]` → `[3, 2]`
✅ **Negative Numbers:** `[-2, -3, 4]` → `[-12, -8, 6]`

## Why This Solution is Optimal

1. **Time Efficient:** O(n) with only two passes
2. **Space Efficient:** O(1) extra space (not counting output)
3. **No Division:** Handles all edge cases naturally
4. **Clean Logic:** Easy to understand and implement
5. **Handles All Cases:** Works with negatives, zeros, etc.

This solution elegantly solves the follow-up challenge while maintaining optimal performance.