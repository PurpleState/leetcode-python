 class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        pointer = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and pointer < len(popped) and stack[-1] == popped[pointer]:
                stack.pop()
                pointer += 1
        return pointer == len(popped)
