"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:
  `1 <= s.length <= 1000`
  `s` is made up of only printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        merged_s = "".join([char for char in s if char.isalnum()]).lower()

        left = 0
        right = len(merged_s) - 1

        while left < right:
            if merged_s[left] != merged_s[right]:
                return False
            left += 1
            right -= 1

        return True


# test
print(Solution().isPalindrome("Was it a car or a cat I saw?"))
print(Solution().isPalindrome("tab a cat"))
