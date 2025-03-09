
class Solution:

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def countPS(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            for j in range(i+1, n):
                if self.isPalindrome(s[i:j+1]):
                    count += 1
        return count
    
    
def test():
    s = Solution()
    print(s.countPS("abaab")) # 3
    print(s.countPS("aaaa")) # 10
    print(s.countPS("abc")) # 3
    print(s.countPS("a")) # 1
    print(s.countPS("")) # 0

test()