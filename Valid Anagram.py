class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
            
        def Counter(str1):
            con = {}
            for c in str1:
                if c in con:
                    con[c] += 1
                else:
                    con[c] = 1
            return con

        counter = Counter(s)

        for i in t:
            if i not in counter:
                return False
            else:
                counter[i] -=1
            
            if counter[i]<0:
                return False
        
        return True
        