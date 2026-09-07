class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpen = {')':'(', '}' : '{', ']':'['}
        for element in s:
            if element in closedToOpen:
                if stack and stack[-1] == closedToOpen[element]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(element)
        if not stack:
            return True
        else:
            return False