'''
First and foremost would be to find the string that has the maximum length as any substring present in it would be present in all 
This gives us more place to check see

Approach the conditions and loop

copyArr = getMainArray
for range(len(copyArr)):
    find smallest string

commonPrefix = []
for each letter in smallest string:
    for all elements in the array:
        if smallest string letter == element string letter:
            commonPrefix.append(letter)
        



'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        workingArray = strs
        commonPrefix = ''
        minString = workingArray[0]
        for word in workingArray:
            if len(word) < len(minString):
                minString = word

        for letterIdx in range(len(minString)):
            testArray = []
            for word in workingArray:
                testArray.append(word[:letterIdx+1])
            testArraySet = set(testArray)
            if len(testArraySet) > 1:
                break
            else:
                commonPrefix = "".join(testArraySet)
        return commonPrefix

strs = ['flower', 'flow', 'flight']
s = Solution()
s.longestCommonPrefix(strs)