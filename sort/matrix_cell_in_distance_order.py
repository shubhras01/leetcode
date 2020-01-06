class Solution(object):
    def valid(self, r,c, i,j):
        if (i>=0 and i <r and j >=0 and j <c):
            return True
        return False

    def allCellsDistOrder1(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        possible = [[0,1],[0,-1],[1,0],[-1,0]]
        cl = [[r0,c0]]
        res = [[r0,c0]]
        cnt = 0
        while cl:
            nl = []
            for i in cl:
                curr = i
                for j in possible:
                    cnt += 1
                    if [curr[0] + j[0], curr[1] + j[1]] not in res and self.valid(R, C, curr[0] + j[0], curr[1] + j[1]):
                        res.append([curr[0] + j[0], curr[1] + j[1]])
                        nl.append([curr[0] + j[0], curr[1] + j[1]])
            cl = nl
        print cnt
        return res

    def allCellsDistOrder(self, R, C, r0, c0):
        all_coord = [[x,y] for y in range(C) for x in range(R)]
        return sorted(all_coord, key=lambda x: abs(x[0]-r0)+abs(x[1]-c0))


if __name__ == "__main__":
    s = Solution()
    inp = [89, 90, 21, 65]
    r = s.allCellsDistOrder(inp[0],inp[1],inp[2],inp[3])
    x = []
    for i in r:
        x.append(abs(i[0]-inp[2])+abs(i[1]-inp[3]))
    print len(x)
    print x, r