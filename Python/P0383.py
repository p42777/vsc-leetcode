class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for i in magazine:
            dict[i] = dict.get(i, 0) + 1
        # print(dict)

        for i in ransomNote:
            if i in dict:
                if(dict[i] >= 1):
                    dict[i] = dict[i] - 1
                else:
                    return False
            else:
                return False

        return True
