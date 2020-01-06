class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in range(len(arr1)):
            d.setdefault(arr1[i],0)
            d[arr1[i]] += 1
        ind = 0
        for i in range(len(arr2)):
            c = arr2[i]
            for j in range(d[c]):
                arr1[ind] = c
                ind += 1
            del d[c]
        r = []
        for i in d.keys():
            r += [i]*d[i]
        r.sort()
        for i in range(len(r)):
            arr1[ind] = r[i]
            ind += 1
        return arr1

if __name__ == "__main__":
    s = Solution()
    print s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])