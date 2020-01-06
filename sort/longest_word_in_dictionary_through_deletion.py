import heapq


class Solution(object):
    def dist(self, s1, s2):
        i,j = 0,0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                j += 1
            i += 1
        if j == len(s2):
            return len(s2)
        return -1

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        heap = []
        for k in d:
            dist = self.dist(s, k)
            heapq.heappush(heap, (-dist, k))
        m = heapq.heappop(heap)
        if m[0] == 1: return ""
        return m[1]


if __name__ == "__main__":
    s = Solution()
    print s.findLongestWord("aewfafwafjlwajflwajflwafj",["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"])

