class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(J)
        total = 0
        for stone in S:
            if stone in J:
                total += 1
        return total