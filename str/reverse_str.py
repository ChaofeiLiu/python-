class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #plan_1
        s.reverse()
        #plan_2
        head = 0
        end  = len(s)-1
        while head < end:
            s[head],s[end] = s[end],s[head]
            head += 1
            end  -= 1
        return s
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        class Solution(object):
            def isPalindrome(self, x):
                """
                :type x: int
                :rtype: bool
                """
                if x < 0:
                    return False
                s = str(x)
                head, end = 0, len(s) - 1
                while head < end:
                    if s[head] == s[end]:
                        head += 1
                        end -= 1
                    else:
                        return False
                return True