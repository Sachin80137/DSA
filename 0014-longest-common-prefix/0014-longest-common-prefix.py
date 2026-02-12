class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        
        prefix = strs[0]
        for i in strs:
            if len(i) < len(prefix):
                prefix = i

        need = len(strs)

        while prefix:
            count = 0

            for i in strs:
                if i[:len(prefix)] == prefix:
                    count += 1

            if count == need:
                return prefix
            else:
                prefix = prefix[:-1]

        return ""
        