class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        m = {}
        for i in S:
            m.setdefault(i,0)
            m[i] += 1
        sortedm = sorted(m.items(), key=lambda x: x[1], reverse=True)
        arr = [sortedm[0][0] for i in range(sortedm[0][1])]
        if sortedm[0][1] > (len(S)+1)/2:
            return ""
        if len(arr) == 1:
            return S
        sortedm.pop(0)
        i,j = 0,0
        while j < len(sortedm):
            ind = -1
            for k in range(sortedm[j][1]):
                ind = i+k if i+k < len(arr) else (i+k)%len(arr)
                arr[ind] = arr[ind]+sortedm[j][0]
            i = ind + 1 if ind != -1 else i+1
            j += 1
        return "".join(arr)


if __name__ == "__main__":
    s = Solution()
    print s.reorganizeString("baaba")
    print s.reorganizeString("aaab")
    print s.reorganizeString("aab")
    print s.reorganizeString("vvvlo")
    print s.reorganizeString("abbabbaaab")
    print s.reorganizeString("kkkkzrkatkwpkkkktrq")