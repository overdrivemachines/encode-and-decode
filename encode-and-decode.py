class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        result = []
        i = 0
        while i < len(str):
            j = i

            # get the length __#
            while str[j] != "#":
                j += 1
            length = int(str[i:j])

            # get the word
            result.append(str[j + 1 : j + 1 + length])

            # beginning of the next word
            i = j + 1 + length

        return result


s = Solution()
input = ["lint", "code", "love", "you"]
encoded = s.encode(input)
print(encoded)
decoded = s.decode(encoded)
print(decoded)
