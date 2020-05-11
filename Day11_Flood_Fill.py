class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def flood(ring,sr,sc,newColor,lenr,lenc):
			for i in range(0,ring):
				
				if sr-i>-1 and sc-ring>-1:
					if image[sr-i+1][sc-ring]==newColor or image[sr-i][sc-ring+1]==newColor:
						image[sr-i][sc-ring]=newColor
				
				if sr+i<lenr and sc+ring<lenc:
					if image[sr+i-1][sc+ring]==newColor or image[sr+i][sc+ring-1]==newColor:
						image[sr+i][sc+ring]=newColor
				
				if sr-ring>-1 and sc-i>-1:
					if image[sr-ring+1][sc-i]==newColor or image[sr-ring][sc-i+1]==newColor:
						image[sr-ring][sc-i]=newColor
				
				if sr+ring<lenr and sc+i<lenc:
					if image[sr+ring-1][sc+i]==newColor or image[sr+ring][sc+i-1]==newColor:
						image[sr+ring][sc+i]=newColor
				
				if sr-i>-1 and sc+ring<lenc:
					if image[sr-i+1][sc+ring]==newColor or image[sr-i][sc+ring-1]==newColor:
						image[sr-i][sc+ring]=newColor
				
				if sr+i<lenr and sc-ring>-1:
					if image[sr+i-1][sc-ring]==newColor or image[sr+i][sc-ring+1]==newColor:
						image[sr+i][sc-ring]=newColor
				
				if sr-ring>-1 and sc+i<lenc:
					if image[sr-ring+1][sc+i]==newColor or image[sr-ring][sc+i-1]==newColor:
						image[sr-ring][sc+i]=newColor
				
				if sr+ring<lenr and sc-i>-1:
					if image[sr+ring-1][sc-i]==newColor or image[sr+ring][sc-i+1]==newColor:
						image[sr+ring][sc-i]=newColor

			if sr-ring>-1 or sr+ring+1<lenr or sc-ring>-1 or sc+ring<lenc:
				flood(ring+1,sr,sc,newColor,lenr,lenc)
			return

		lenr=len(image)
		lenc=len(image[0])
		image[sr][sc]=newColor
		flood(1,sr,sc,newColor,lenr,lenc)