class Solution(object):
    def search(self, arr, key, l):
        r = len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < key:
                l = mid + 1
            else:
                r = mid
        if l < len(arr) and arr[l] == key:
            return l
        return -1

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        arr_big, arr_small = [nums1, nums2] if len(nums1) > len(nums2) else [nums2, nums1]
        lo = 0
        res = []

        for i in arr_small:
            found = self.search(arr_big, i, lo)
            if found != -1:
                res.append(i)
                lo = found + 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.intersect([61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,66,82,0,79,11,81]
,[5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48]))
    arr1 = [61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,66,82,0,79,11,81]
    arr2 = [5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48]
    arr1.sort()
    arr2.sort()
    print(arr1)
    print(arr2)
    res = [x for x in arr1 if x in arr2]
    res.sort()
    x = [5,4,57,79,7,89,88,45,34,92,38,85,6,0,77,44,61]
    x.sort()
    d1 = {}
    d2 = {}
    for i in arr1:
        d1.setdefault(i,0)
        d1[i] += 1
    for i in arr2:
        d2.setdefault(i,0)
        d2[i]+=1
    for i in res:
        print(i, d1[i], d2[i])
    print(x)