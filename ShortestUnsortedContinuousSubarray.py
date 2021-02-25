'''find the first inverse pair from the start as l;
find the first inverse pair from the end as r;
find min_val and max_val of [l ,r];
using binary search to find the position of min_val to insert into in [0, l];
using binary search to find the position of max_val to insert into in [r, end];'''

def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2: return 0
		
        l, r = 0, len(nums)-1
        while l < len(nums) - 1 and nums[l] <= nums[l+1]:
            l += 1
        if l == len(nums) - 1: return 0
        while r > 0 and nums[r] >= nums[r-1]:
            r -= 1
			
        mmin = mmax = nums[l]
        for i in range(l+1, r+1):
            mmin, mmax = min(mmin, nums[i]), max(mmax, nums[i])
			
        lpos = bisect_right(nums[:l+1], mmin)
        rpos = bisect_left(nums[r:], mmax) + r
        return rpos - lpos
