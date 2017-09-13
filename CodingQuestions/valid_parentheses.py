"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}"
are all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stk.append(ch)
            else:
                if len(stk) == 0:
                    return False
                open_parenthesis = stk.pop()
                if ch == ']' and open_parenthesis != '[':
                    return False
                elif ch == ')' and open_parenthesis != '(':
                    return False
                elif ch == '}' and open_parenthesis != '{':
                    return False
        return len(stk) == 0
