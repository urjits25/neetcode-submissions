class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # maintain the product of left part without self
        # similarly maintain product of right part without self
        # multiply them together and return the array

        lprod = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            lprod[i] = lprod[i-1] * nums[i-1]
        
        rprod = 1
        for j in range(len(nums)-2, -1, -1):
            rprod *= nums[j+1]
            lprod[j] *= rprod
        return lprod
