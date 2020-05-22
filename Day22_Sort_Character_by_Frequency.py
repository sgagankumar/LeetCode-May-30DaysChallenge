class Solution:
	def frequencySort(self, s: str) -> str:
		from collections import Counter
		Counts=dict(Counter(s))
		Countsorted={k: v for k, v in sorted(Counts.items(), key=lambda item: item[1])}
		output=''
		for char,count in Countsorted.items():
			output+=char*count
		return output[::-1]