class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:
            return []
        res = []
        S = list(S)
        size = len(S)
        idx = 0

        def dfs(S, size, idx, res):
            if idx == size:
                tmp = ''.join(S)
                return res.append(tmp)

            dfs(S, size, idx + 1, res)
            if S[idx].isalpha():
                if S[idx].islower():
                    S[idx] = S[idx].upper()
                elif S[idx].isupper():
                    S[idx] = S[idx].lower()
                dfs(S, size, idx + 1, res)
                # print(S)

        dfs(S, size, idx, res)
        return res
