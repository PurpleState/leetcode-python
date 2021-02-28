class FreqStack(object):

    def __init__(self):
        self.freq = Counter()
        self.stacks = defaultdict(list)
        self.maxfreq = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        freq_x = self.freq[x] + 1
        self.freq[x] = freq_x
        self.maxfreq = max(self.maxfreq, freq_x)
        self.stacks[freq_x].append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        x = self.stacks[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.stacks[self.maxfreq]: self.maxfreq -= 1
        return x
        
#problem: do I use a stack or which ds to use, -> array?

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
