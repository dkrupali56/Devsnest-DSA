def solve(str):
    
    stack=[]

    brackets={"(":")","{":"}","[":"]"}

    for bracket in str:
        
        # Push Opening bracket in stack
        if bracket in brackets.keys():
            stack.append(bracket)

        # Pop matched bracket from stack. Stack will always store only opening brakets.
        elif len(stack)!=0 and brackets[stack[-1]]==bracket:

            stack.pop()

        # Unmatched bracket return False
        else:
            return 0

    # Check whether all brackets gets matched or not
    if len(stack)==0:
        return 1

    return 0
