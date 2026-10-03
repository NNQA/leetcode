class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        for i in range(1, len(words)):
            words[0] = "".join((Counter(words[0]) & Counter(words[i])).elements())
        return list(words[0])

    def commonChars1(self, words: list[str]) -> list[str]:
        res = []
        for c in range(ord("a"), ord("z") + 1):
            char = chr(c)
            min_freq = float(inf)
            for word in words:
                freq = word.count(char)
                min_freq = min(min_freq, freq)
                if min_freq == 0:
                    break
            res.extend([char] * min_freq)
        return res
