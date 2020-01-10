class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in range(k):
            for j in range(i+1, k):
                if j >= len(nums): break
                if abs(nums[i] - nums[j]) <= t:
                    return True
        for i in range(1,len(nums)):
            for j in range(k):
                if i+j >= len(nums): break
                if i+k >= len(nums): break
                if abs(nums[i+j]-nums[i+k]) <= t:
                    return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))
    print(s.containsNearbyAlmostDuplicate([2,2],3,0))
    print(s.containsNearbyAlmostDuplicate([0],0,0))




