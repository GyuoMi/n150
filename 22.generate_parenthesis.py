class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # valid once we reach closed == open == n
        # only can add a ) if close < open
        # only add open ( if open < n
        
        res = []
        stack = [] # to keep track of paranthesis 

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
                
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

        backtrack(0,0)
        return res