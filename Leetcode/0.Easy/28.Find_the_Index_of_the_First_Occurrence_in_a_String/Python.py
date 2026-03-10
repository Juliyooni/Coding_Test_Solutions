# Solution 1
# C# Style Solution
# runtime : 0ms, memory : 19.41MB


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for x in range(len(haystack) - len(needle) + 1):
            i = 0

            if haystack[x] == needle[i]:
                i += 1
                if i == len(needle):
                    return x

                for y in range(x + 1, x + len(needle)):
                    if haystack[y] == needle[i]:
                        i += 1
                        if i == len(needle):
                            return x

                    else:
                        break

        return -1


# Solution 2
# Pythonic Solution, using slicing
# runtime : 0ms, memory : 19.28MB


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for x in range(len(haystack) - len(needle) + 1):
            if haystack[x : x + len(needle)] == needle:
                return x

        return -1
