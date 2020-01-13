class Solution(object):
    def search(self, arr, key):
        lo = 0
        hi = len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < key:
                lo = mid + 1
            else:
                hi = mid
        if lo < len(arr):
            return arr[lo]
        return None

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        arr_sm, arr_bi = [nums1, nums2] if len(nums1) < len(nums2) else [nums2, nums1]
        res = []
        last = None
        for i in arr_sm:
            found = self.search(arr_bi, i)
            print(found)
            if found != None and found == i and i != last:
                res.append(i)
                last = i

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.intersection([8,0,3],[0,0]))
