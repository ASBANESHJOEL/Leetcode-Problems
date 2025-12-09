class Solution(object):
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        right = {}
        left = {}
    
        for x in nums:
            right[x] = right.get(x, 0) + 1

        ans = 0

        for j in range(len(nums)):
            val = nums[j]
        
            right[val] -= 1
            if right[val] == 0:
                del right[val]
        
            target = val * 2
        
            if target in left and target in right:
                ans = (ans + left[target] * right[target]) % MOD
        
            left[val] = left.get(val, 0) + 1

        return ans % MOD
