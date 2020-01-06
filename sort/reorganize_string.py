class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        m = {}
        for i in S:
            m.setdefault(i,0)
            m[i] += 1
        sortedm = sorted(m.items(), key=m.get, reverse=True)
        print sortedm
        arr = []


if __name__ == "__main__":
    s = Solution()
    print s.reorganizeString("baaba")