class Solution:
	def removeKdigits(self, num: str, k: int) -> str:
		num=list(map(int,num))
		if(len(num)==k):
			return '0'
		while(k>0):

			if len(num)>=2:
				if num[0]>=num[1]:
					print(num.pop(0))
					k-=1
					continue
				
			flag=False
			for i in range(1,len(num)-1):
				if num[i]>num[i-1] and num[i]>=num[i+1]:
					print(num.pop(i))
					flag=True
					k-=1
					break
			if(flag):
				continue
			
			print(num.pop())
			k-=1

			
		#return string
		s=''
		for n in num:
			s+=str(n)
		return str(int(s))
				