class Solution(object):
    def cmp_to_key(self, mycmp):
        class K:
            def __init__(self, obj, *args):
                self.obj = obj

            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0

            def __gt__(self, other):
                return mycmp(self.obj, other.obj) > 0

            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0

            def __le__(self, other):
                return mycmp(self.obj, other.obj) <= 0

            def __ge__(self, other):
                return mycmp(self.obj, other.obj) >= 0

            def __ne__(self, other):
                return mycmp(self.obj, other.obj) != 0

        return K

    def less(self, num1, num2):
        alldigs1 = list(map(int, list(str(num1))))
        alldigs2 = list(map(int, list(str(num2))))
        i=0
        while i < len(alldigs1) and i < len(alldigs2) and alldigs1[i] == alldigs2[i]:
            i += 1
        if i >= len(alldigs1):
            return num1
        if i >= len(alldigs2):
            return -num2
        return alldigs1[i] - alldigs2[i]

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        print(sorted(list(map(str, nums)), reverse=True))
        return  "".join(list(map(str,  sorted(nums, key=self.cmp_to_key(self.less), reverse=True))))


if __name__ == "__main__":
    s = Solution()
    print(s.largestNumber([10,2]))
    print(s.largestNumber([3,30,34,5,9]))
    print(s.largestNumber([9,91,910,9100,10]))


