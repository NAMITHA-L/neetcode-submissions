class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i in "([{":
                l.append(i)
            elif i in ")}]":
                if not l:return False
                else:
                    if l[-1] == "(" and i == ")":l.pop()
                    elif l[-1] == "[" and i == "]":l.pop()
                    elif l[-1] == "{" and i == "}":l.pop()
                    else: return False
        return len(l)==0
