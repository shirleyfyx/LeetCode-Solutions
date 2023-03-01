class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for c in s:
            if c in hash_map.values():
                stack.append(c)
                continue
            if c in hash_map.keys():
                if hash_map[c] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
