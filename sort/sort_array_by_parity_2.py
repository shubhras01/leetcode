class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        IndexO = 1
        IndexE = 0
        while IndexE < len(A) and IndexO < len(A):
            if A[IndexE]%2 == 1:
                A[IndexE], A[IndexO] = A[IndexO], A[IndexE]
                IndexO += 2
            else:
                IndexE += 2
        return A


if __name__ == "__main__":
    s = Solution()
    print s.sortArrayByParityII([648,831,560,986,192,424,997,829,897,843])