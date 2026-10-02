class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        iterated 2sum
        sorted 2sum? 
        to remove duplicates, ensure the nums[i] is not the same
        '''

        res = []
        nums.sort()
        N = len(nums)
        for i in range(N-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            target = -nums[i]
            j, k = i+1, N-1
            while j > i and k < N and j < k:
                cur_sum = nums[j] + nums[k]
                if target == cur_sum:
                    res.append([nums[i], nums[j], nums[k]] )
                    j += 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                
                    k -= 1
                    
                elif target > cur_sum:
                    j += 1
                else:
                    k -= 1
        return res