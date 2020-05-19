class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:
		output=list()
		p=list(p)
		p.sort()
		s=list(s)
		i=0
		plen=len(p)
		slen=len(s)
		while(i<(slen-plen+1)):
			x=s[i:i+plen]
			# print(x)
			x.sort()
			if(x==p):
				output.append(i)
				flag=True
				while(flag and i<(slen-plen)):
					if s[i]==s[i+plen]:
						i+=1
						output.append(i)
					else:
						flag=False 
			i+=1
		return output
