# https://leetcode.com/problems/remove-duplicate-letters/

def removeDuplicateLetters(self, s: str):
        last_idx = {c:i for i, c in enumerate(s)}
        visited = set()
        stack = []
        
        for i in range(len(s)):
            if s[i] in visited:
                continue
            else:
                while stack and s[i] < stack[-1] and last_idx[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
        
        return ''.join(stack)