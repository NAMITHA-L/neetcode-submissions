class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []
        
        for i in tokens:                
            if i in "+-*/":
                a = l[-1]
                b = l[-2]
                l.pop()
                l.pop()
                if i == "+": 
                    l.append(a+b)
                if i == "-":
                    l.append(b-a)
                if i == "*":
                    l.append(a*b)
                if i == "/":
                    l.append(int(b/a))
            else:l.append(int(i))
        return l[0]