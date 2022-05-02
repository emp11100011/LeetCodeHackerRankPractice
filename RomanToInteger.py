class Solution:
    def romanToInt(self, s: str) -> int:
        romanData = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        romanNum = [romanData[x] for x in s]
        total = 0
        i = 0
        while i <= len(romanNum)-1:
            if i + 1 < len(romanNum):
                if romanNum[i] >= romanNum[i+1]:
                    total = total + romanNum[i]
                    i = i + 1
                elif romanNum[i] < romanNum[i+1]:
                    total = total + (romanNum[i+1] - romanNum[i])
                    if i + 2 <= len(romanNum):
                        i = i + 2
            else:
                total = total + romanNum[i]
                break
        return total

j = Solution()
j.romanToInt('III')