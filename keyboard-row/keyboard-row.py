class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        v1 = 'qwertyuiopQWERTYUIOP'
        v2 = 'asdfghjklASDFGHJKL'
        v3 = 'zxcvbnmZXCVBNM'
        ans = []
        for word in words:
            # a = list(word)
        #     if all(letter in v1 for letter in word):
        #         ans.append(word)
        #     elif all(letter in v2 for letter in word):
        #         ans.append(word)
        #     elif all(letter in v3 for letter in word):
        #         ans.append(word)
        # return ans
            # d = {a1: 0, a2: 0, a3: 0}
            a1 = False
            a2 = False
            a3 = False
            for letter in word:
                if letter in v1:
                    a1 = True
                elif letter in v2:
                    # print('1')
                    a2 = True
                else:
                    a3 = True
                if (a1 & a2) or (a1 & a3) or (a2 & a3):
                    break
            if (a1 & a2) or (a1 & a3) or (a2 & a3):
                    continue
            str1 = ''
            
            ans.append(str1.join(word))
        return ans