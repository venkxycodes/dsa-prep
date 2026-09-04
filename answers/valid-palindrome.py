class Solution:
    def isPalindrome(self, s: str) -> bool:
        curated_string = ''
        for char in s:
            if ord(char) >= 48 and ord(char) <= 57:
                curated_string += char
            elif ord(char) >= 65 and ord(char) <= 90:
                curated_string += char.lower()
            elif ord(char) >= 97 and ord(char) <= 122:
                curated_string += char.lower()
        # print(curated_string)
        # print(len(curated_string))
        if curated_string == "": return True
        left, right = 0, len(curated_string)-1
        while left <= right:
            # print(left, right)
            if curated_string[left] != curated_string[right]:
                return False
            left += 1
            right -= 1
        return True