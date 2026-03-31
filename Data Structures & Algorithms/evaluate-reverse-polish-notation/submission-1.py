class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        symbols = set(["*","+","/","-"])
        for token in tokens:
            if token in symbols:
                tmp = None
                for _ in range(2):
                    if tmp == None:
                        tmp = int(result.pop())
                    else:
                        op = int(result.pop())
                        if token == "*":
                            tmp = op * tmp
                        elif token == "+":
                            tmp = op + tmp
                        elif token == "/":
                            tmp = int(op / tmp)
                        elif token == "-":
                            tmp = op - tmp
                result.append(tmp)
            else:
                result.append(token)

        return int(result[0])