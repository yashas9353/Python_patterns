class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        if x > 0:
            while x>0:
                rem = x%10
                reverse = (reverse*10)+rem
                x = x//10
        else:
            x = abs(x)
            while x>0:
                rem = x%10
                reverse = (reverse*10)+rem
                x = x//10
            reverse = -reverse
        if reverse > (2**31 - 1) or (reverse < -2**31):
            return 0
        else: 
            return reverse