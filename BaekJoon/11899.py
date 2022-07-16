inputs = input()
stack = []
for i in range(len(inputs)):
    if(inputs[i] == '('):
        stack.append('(')
    elif (inputs[i] == ')'):
        if (len(stack) and stack[-1] == '('):
            stack.pop()
        else :
            stack.append(')')
    else :
        print("ERROR input is invalid")
        exit()
print(len(stack))