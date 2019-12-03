class Solution(object):
	def canVisitAllRooms(self, rooms):
		"""
		:type rooms: List[List[int]]
		:rtype: bool
		"""
		queue = [x for x in rooms[0]]
		visited = [False for i in rooms]
		visited[0] = True
		while queue:
			cRoom = queue.pop(0)
			visited[cRoom] = True
			queue += [x for x in rooms[cRoom] if not visited[x]]
		not_visited = filter(lambda x: not x, visited)
		if not_visited:
			return False
		return True





