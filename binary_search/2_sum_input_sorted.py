class Solution1(object):
    def search(self, arr, key):
        lo, hi = [0, len(arr)]
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < key:
                lo = mid + 1
            else:
                hi = mid

        if lo < len(arr):
            return lo
        return None

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(numbers) - 1):
            cand1 = numbers[i]
            found = self.search(numbers[i + 1:], target - cand1)
            if found != None and numbers[i + 1 + found] + cand1 == target:
                return [i + 1, i + 2 + found]


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(numbers)):
            cand = target - numbers[i]
            if cand in d:
                return [i+1, d[cand]+1]
            d[numbers[i]] = i


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))