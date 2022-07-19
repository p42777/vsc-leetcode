class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        map = { ")" : "(", "}" : "{", "]" : "["} # HashMap for parenthesis

        for char in s:
            if char in map:
                if stack and stack[-1] == map[char]: # top == matching parenthesis
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if not stack:
            return True
        else:
            return False


