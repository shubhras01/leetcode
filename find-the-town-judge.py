class Solution(object):
	def findJudge(self, N, trust):
		"""
		:type N: int
		:type trust: List[List[int]]
		:rtype: int
		"""
		inc_degree = [0 for i in range(N)]
		for i in range(len(trust)):
			a,b = trust[i]
			inc_degree[a-1] -= 1
			inc_degree[b-1] += 1
		for i in range(N):
			if inc_degree[i] == N-1:
				return i+1

		return -1
