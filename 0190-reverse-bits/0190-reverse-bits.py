class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:].zfill(32)
        
        # Reverse the string
        rev = n[::-1]
        
        # Convert the reversed string back to an integer
        return int(rev, 2)