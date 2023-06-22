def solve(infix):
    
    postfix=[]

    stack=[]

    precedence={"+":1,"-":1,"*":2,"/":2,"^":3,"(":4}

    for ch in infix:
        
        if ch in precedence.keys():
    
            while stack and stack[-1]!="(" and precedence[stack[-1]]>= precedence[ch]:

                postfix.append(stack.pop())
            stack.append(ch)

        elif ch==")":

            # Pop all until opening bracket is encounterd

            while 1:
                x=stack.pop()
                if x!="(":
                    postfix.append(x)
                else:
                    break
        elif ch !="(":
            # Means this is not opeartor it is operand
            # Append charcters in postfix
            postfix.append(ch)

        else:
            stack.append(ch)
    
    # Empty srtack if something is left.
    while stack:
        postfix.append(stack.pop())
    
    return "".join(postfix)
