import heapq


class pq(object):
    arr = []
    N = 0

    def less(self, a, i, j):
        p1 = a[i]
        p2 = a[j]
        d1 = (p1[0] ** 2 + p1[1] ** 2) ** 0.5
        d2 = (p2[0] ** 2 + p2[1] ** 2) ** 0.5
        return d1 <= d2

    def swim(self, a, k, n):
        while (k > 1 and self.less(a, k / 2, k)):
            a[k / 2], a[k] = a[k], a[k / 2]
            k = k / 2

    def sink(self, a, k, n):
        while (2 * k <= n):
            j = 2 * k
            if a[j] < a[j + 1]:
                j += 1
            if not self.less(k, j): break
            a[k], a[j] = a[j], a[k]
            k = j

    def insert(self, key):
        self.arr.append(key)
        self.N += 1
        self.swim(self.arr, len(self.arr) - 1, self.N)

    def delMax(self):
        m = self.arr[0]
        self.arr[0], self.arr[self.N - 1] = self.arr[self.N - 1], self.arr[0]
        self.sink(self.arr, 1, self.N)
        return m


class Solution(object):

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        for i in points:
            x,y = i
            dist = -(x*x+y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [(x,y) for (dist,x,y) in heap]


