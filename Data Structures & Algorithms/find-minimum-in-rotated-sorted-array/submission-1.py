class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        binary search 
        - find mid
        - check if min can be in the left or right subarry
        - recurse till single element OR both neighbors are bigger than mid
        '''
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if mid > 0 and mid < len(nums)-1 and \
              nums[mid-1] > nums[mid] < nums[mid+1]:
                return nums[mid]
            
            # if cur subarray is rotated
            if nums[l] > nums[r]:
                if nums[l] > nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # if cur subarray is not rotated
            else:
                break
        return nums[l]