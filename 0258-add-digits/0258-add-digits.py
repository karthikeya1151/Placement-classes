class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        for digit in str(num):
            sum += int(digit)
        if len(str(sum)) == 1:
            return int(sum)
        else:
            return self.addDigits(sum)