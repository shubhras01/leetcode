class dfu:
	def __init__(self, n):
		self.p = range(n)

	def union(self, x, y):
		p_x = self.find(x)
		p_y = self.find(y)
		self.p[p_y] = p_x

	def find(self, x):
		while self.p[x] != x:
			x = self.p[x]
		return self.p[x]


class Solution(object):

	def findRedundantConnection(self, edges):
		"""
		:type edges: List[List[int]]
		:rtype: List[int]
		"""
		n = []
		for e in edges:
			n.append(e[0])
			n.append(e[1])
		n = list(set(n))
		cdfu = dfu(len(n))
		pans = []

		for e in edges:
			if cdfu.find(e[0]-1) != cdfu.find(e[1]-1):
				cdfu.union(e[0]-1, e[1]-1)
			else: pans.append(e)
		return pans[-1]


if __name__ == "__main__":
	sol = Solution()
	inp = [[1,4],[3,4],[1,3],[1,2],[4,5]]
	print sol.findRedundantConnection(inp)

