def generateParenthesis(self, n: int) -> List[str]:
    result = []

    def generate(open, close, curr):
        if open == close == 0:
            result.append(curr)
        if open > 0:
            generate(open - 1, close, curr + "(")
        if open < close:
            generate(open, close - 1, curr + ")")

    generate(n, n, "")
    return result