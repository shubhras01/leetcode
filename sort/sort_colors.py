class Solution(object):
    def sort(self, arr, lo, hi):
        if hi <= lo:
            return
        lt = lo
        i = lt +1
        gt = hi
        v = arr[lo]
        while i <= gt:
            cmp = arr[i] - v
            if cmp < 0:
                arr[i],arr[lt] = arr[lt],arr[i]
                i += 1
                lt += 1
            elif cmp > 0:
                arr[i],arr[gt] = arr[gt],arr[i]
                gt -= 1
            else:
                i += 1
        self.sort(arr, lo, lt-1)
        self.sort(arr, gt+1, hi)

    def sortColors(self, nums):
        """
        :param nums:
        :return: None, modify arr in place
        """
        if not nums:
            return []
        self.sort(nums, 0, len(nums)-1)


if __name__ == "__main__":
    s = Solution()
    arr = [2,0,2,1,1,0]
    arr = [0,0,1,1,2,2,2,2,2,6,7,0]
    arr = [2]
    s.sortColors(arr)
    print arr


