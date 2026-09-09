class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = []
        for element in s:
            if element.isalnum():
                output.append(element.lower())
        
        return output == output[::-1]