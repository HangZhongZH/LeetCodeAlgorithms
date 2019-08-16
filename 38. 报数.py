class Solution:
    def countAndSay(self, n: int) -> str:
        count = 1
        ans = '1'

        def countword(string):
            m = 1
            word = [string[0]]
            wordcount = []
            for i in range(1, len(string)):
                if string[i] == string[i - 1]:
                    m += 1
                else:
                    word.append(string[i])
                    wordcount.append(m)
                    m = 1
            if len(wordcount) < len(word):
                wordcount.append(m)
            return word, wordcount

        while count < n:
            word, wordcount = countword(ans)
            ans = ''
            for idx1, item1 in enumerate(word):
                for idx2, item2 in enumerate(wordcount):
                    if idx1 == idx2:
                        ans += str(item2) + item1
            count += 1
        return ans