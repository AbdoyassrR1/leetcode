#!/usr/bin/python3

def isvalidation(s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False
        validation = False
    
        if len(s) > 1:
            for i in range(len(s)):
                if i == (len(s) - 1):
                    break
                if s[i] == "(" and s[i + 1] == ")":
                    validation = True
                elif s[i] == "{" and s[i + 1] == "}":
                    validation = True
                elif s[i] == "[" and s[i + 1] == "]":
                    validation = True
                else:
                    validation = False
                i += 1
        return validation

print(isvalidation("()"))
print(isvalidation("()[]{}"))
print(isvalidation("(]"))
