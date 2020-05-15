class Solution:
	def maxSubarraySumCircular(self, A: List[int]) -> int:
		maxFinal = A[0] 
		maxTemp = A[0]
		maxl = list(A)
		maxr = list(A)
		suml=0
		sumr=0
		size=len(A)
		
		for i in range(1,size):
			maxTemp = max(A[i],maxTemp+A[i])
			maxFinal = max(maxFinal,maxTemp)
			
		for i in range(size):
			suml=suml+A[i]
			maxl[i]=suml
			sumr=sumr+A[size-i-1]
			maxr[i]=sumr
		
		maxTemp = A[0]
		for i in range(1,size-1):
			maxTemp = max(maxl[:i])+max(maxr[:-i])
			maxFinal = max(maxFinal,maxTemp)
		
		return maxFinal