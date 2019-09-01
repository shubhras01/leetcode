class Solution(object):
	def maxLevelSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		marker = None
		queue = [root, marker]
		max_sum = 0
		c_sum = 0
		max_level = 0
		c_level = 1
		while len(queue) > 1:
			a = queue.pop(0)
			if a != marker:
				c_sum += a.val
				if a.left: queue.append(a.left)
				if a.right: queue.append(a.right)
			else:
				if c_sum > max_sum:
					max_level, max_sum = c_level, c_sum
				queue.append(None)
				c_level += 1
				c_sum = 0
		return max_level
