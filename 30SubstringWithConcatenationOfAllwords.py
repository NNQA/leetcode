class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        charWordLength = len(words[0])
        word_count = {}
        result = []
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        for i in range(charWordLength):
            left = i
            sub_count = {}
            count = 0
            for j in range(i, len(s) - charWordLength + 1, charWordLength):
                sub_word = s[j : j + charWordLength]
                if sub_word in word_count:
                    if sub_word in sub_count:
                        sub_count[sub_word] += 1
                    else:
                        sub_count[sub_word] = 1
                    count += 1
                    while sub_count[sub_word] > word_count[sub_word]:
                        sub_count[s[left : left + charWordLength]] -= 1
                        count -= 1
                        left += charWordLength

                    if count == len(words):
                        result.append(left)
                else:
                    sub_count.clear()
                    count = 0
                    left = j + charWordLength

        return result


sol = Solution()
print(sol.findSubstring("barfoofoobarthefoobarman", ["foo", "bar"]))
