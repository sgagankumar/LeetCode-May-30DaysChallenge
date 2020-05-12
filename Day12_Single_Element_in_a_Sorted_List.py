class Solution:
    def singleNonDuplicate(self, n: List[int]) -> int:
        ele=0
        for i in n:
            ele=ele^n
        return ele