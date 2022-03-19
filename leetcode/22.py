# https://leetcode.com/problems/generate-parentheses/

# 내 풀이
def generateParenthesis(self, n: int):
        def check(s):
            l = 0
            for v in s:
                if l >= 0 and v == '(':
                    l+=1
                elif l <= 0 and v == ')':
                    return False
                else:
                    l-=1
            return True if l == 0 else False
        
        def dfs(left,right,arr,s):
            if left:
                dfs(left-1,right,arr,s+'(')
            if right:
                dfs(left,right-1,arr,s+')')
            if not left and not right:
                arr.append(s)
        
        res =[]
        dfs(n,n,res,"")
        ans = []
        for v in res:
            if check(v):
                ans.append(v)
        return ans

# 제대로 된 풀이
def generateParenthesis(self, n: int):
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
