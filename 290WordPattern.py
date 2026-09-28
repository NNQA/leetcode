class Solution:
    # beat 100%
    def wordPattern1(self, pattern: str, s: str) -> bool:

        words = s.split()
        if len(pattern) != len(words):
            return False

        mapP = {}
        mapS = {}
        for i, (p_char, word) in enumerate(zip(pattern, words), start=1):
            if mapP.get(p_char) != mapS.get(word):
                return False
            mapP[p_char] = i
            mapS[word] = i

        return True

    def wordPattern(self, pattern: str, s: str) -> bool:

        word = s.split()
        return len(set(pattern)) == len(set(s)) == len(set(zip(pattern, s)))


print(Solution().wordPattern("abba", "dog cat cat dog"))
