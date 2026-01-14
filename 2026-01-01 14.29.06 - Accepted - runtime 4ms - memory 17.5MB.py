class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1  # n for base[n]
        if n < 1:
            return False
        
        # Expected: [1, 2, ..., n-1, n, n]
        # Check if sorted nums matches expected
        nums.sort()
        
        for i in range(n - 1):
            if nums[i] != i + 1:
                return False
        
        # Last two elements should both be n
        return nums[n - 1] == n and nums[n] == n