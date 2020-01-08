class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution1(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        def getStart(i):
            return i.start
        intervals.sort(key = getStart)
        for i in intervals:
            print [i.start, i.end],
        li,lj = intervals[0].start, intervals[0].end
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if li <= intervals[i].start and lj >= intervals[i].start:
                lj = max(lj, intervals[i].end)
                res.pop()
                res.append(Interval(li,lj))
            else:
                li, lj = intervals[i].start, intervals[i].end
                res.append(Interval(li,lj))
        return res


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        # print intervals
        i = 0
        j = 1
        lt = -1
        st = 0
        res = []
        while j <len(intervals):
            lt = intervals[i][1]
            lt_last = lt
            st = intervals[j][0]
            while lt >= st:
                lt_last = lt
                lt = max(lt_last, intervals[j][1])
                j += 1
                if j >= len(intervals): break
                st = intervals[j][0]
            new_int = [intervals[i][0], lt]
            res.append(new_int)
            i = j
            j += 1
        if i < len(intervals):
            res.append([intervals[i][0],intervals[i][1]])
        return res


if __name__ == "__main__":
    s = Solution()
    s1 = Solution1()
    print s.merge([[1,10],[15,18]])
    print s.merge([[1,3],[2,6],[6,8],[8,10],[15,18],[18,20]])
    print s.merge([[1,3],[2,6],[8,10],[15,18]])
    print s.merge([[1,4],[4,5]])
    print s.merge([[1,4],[0,4]])
    print s.merge([[1,4],[2,3]])
    print s.merge([[5,5],[1,3],[3,5],[4,6],[1,1],[3,3],[5,6],[3,3],[2,4],[0,0]])
    # arr = [[5,5],[1,3],[3,5],[4,6],[1,1],[3,3],[5,6],[3,3],[2,4],[0,0]]
    # intervals = []
    # for i in arr:
    #     ii = Interval(s=i[0],e=i[1])
    #     intervals.append(ii)
    # print s.merge(arr)
    # print s1.merge(intervals)