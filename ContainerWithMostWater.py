class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        maxarea = 0
        while i<j:
            maxarea = max(maxarea, min(height[i], height[j])*(j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxarea
        
