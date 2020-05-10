class Solution:
	def findJudge(self, n: int, trust: List[List[int]]) -> int:
		trustedBy=[]
		trustee=[]
		for i in range(n+1):
			trustedBy.append([])
		for (x,y) in trust:
			trustedBy[y].append(x)
			trustee.append(x)
		for i in range(1,n+1):
			if (len(trustedBy[i])==n-1):
				if (i not in trustee):
					return i
		return -1