class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in barcodes:
            d.setdefault(i, 0)
            d[i] += 1

        sortedd = sorted(d.items(), key=lambda x: x[1], reverse=True)

        arr = [[sortedd[0][0]] for i in range(sortedd[0][1])]
        sortedd.pop(0)
        i = 0
        for j in sortedd:
            ind = -1
            for k in range(j[1]):
                ind = i + k if i + k < len(arr) else (i + k) % len(arr)
                arr[ind].append(j[0])
            i = ind + 1 if ind != -1 else i + 1

        return [x for y in arr for x in y]


if __name__ == "__main__":
    s = Solution()
    print s.rearrangeBarcodes([1,1,1,1,2,2,3,3])
    print s.rearrangeBarcodes([1,1,1,2,2,2])
