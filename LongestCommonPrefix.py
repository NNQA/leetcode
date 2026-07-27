
# 0ms 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        temp = ""
        len_of_strs = len(strs)
        i = 0
        for char in first:
            temp += char
            re = False
            while i < len_of_strs:
                if not strs[i].startswith(temp):
                    re = True
                    break
                i += 1
            i = 0
            if re:
                temp=temp[:-1]
                break
        return temp
    

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))  
