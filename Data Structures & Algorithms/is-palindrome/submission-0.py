class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = ""
        for i in s:
            if i.isalnum():
                reverse += i.lower()
        last = len(reverse)-1
        news = ['0'] * len(reverse)

        for i in range(len(reverse)):
            if(last >= i):
                news[i] = reverse[last]
                news[last] = reverse[i]
            last -= 1
        return list(reverse) == news

