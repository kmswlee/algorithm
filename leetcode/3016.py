from collections import Counter

def minimumPushes(self, word: str) -> int:
        counter = Counter(word)

        if counter.total() < 9:
            return counter.total()
        
        res = 0
        idx = 1
        for i,v in counter.most_common(26):
            if idx < 9:
                res += (v * 1)
            elif idx < 17:
                res += (v * 2)
            elif idx < 25:
                res += (v * 3)
            else:
                res += (v * 4)
            
            idx += 1
        
        return 

# other solution
def minimumPushes(self, word: str) -> int:
        l=[0]*(32)
        for i in range(26):
            l[i]=word.count(chr(97+i))
        l.sort(reverse=True)
        res=0
        for i in range(4):
            for j in range(8):
                res+=(i+1)*l[8*i+j]
        return res
