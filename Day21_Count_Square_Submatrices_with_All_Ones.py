class Solution:
	def isSmallest(self, root, k, n, output):
		if root.left and output==-1:
			n, output=self.isSmallest(root.left, k, n, output)
		n+=1
		if n==k:
			output=root.val
		
		print(root.val,',',n)
		if root.right and output==-1:
			n, output=self.isSmallest(root.right, k, n, output)
		return n, output
			
		
	
	
	def kthSmallest(self, root: TreeNode, k: int) -> int:
		_ , output = self.isSmallest(root, k, 0, -1)
		return output