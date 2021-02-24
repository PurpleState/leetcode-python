''' Problem: https://leetcode.com/problems/search-a-2d-matrix-ii/
Best Explanation: https://www.youtube.com/watch?v=FOa55B9Ikfg 
Complete Solution: http://twistedoakstudios.com/blog/Post5365_searching-a-sorted-matrix-faster '''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        return False
                
        
        
