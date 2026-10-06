class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = []
        for s in strs:
            ans.append("{:4}".format(len(s)) + s)
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        ans = []
        i, n = 0, len(s)
        while i < n:
            size = int(s[i : i + 4])
            i += 4
            ans.append(s[i : size + 4])
            i += size
        return ans


a = Solution()
encoded_str = a.encode(["quoc", "anh"])
print("Encoded:", repr(encoded_str))

decoded_list = a.decode(encoded_str)
print("Decoded:", decoded_list)
