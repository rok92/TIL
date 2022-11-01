T = int(input())
for test_case in range(1, T + 1):
    cal = list(input().split())
    stack = []
    print("#", test_case,' ', sep='', end="")

    for i in range(len(cal)) :
        # 숫자일 경우 스택에 쌓기
        if cal[i].isdigit() :
            stack.append(int(cal[i]))
        if cal[i] == '.' :
            if len(stack) == 1 :
                print(stack.pop())
                break
            else :
                print('error')
                break
        if cal[i] =='+' :
            if len(stack) > 1 :
                stack.append(stack.pop(-2) + stack.pop(-1))
            else :
                print('error')
                break
        elif cal[i] =='-' :
            if len(stack) > 1 :
                stack.append(stack.pop(-2) - stack.pop(-1))
            else : 
                print('error')
                break
        elif cal[i] =='*' :
            if len(stack) > 1 :
                stack.append(stack.pop(-2) * stack.pop(-1))
            else :
                print('error')
                break
        elif cal[i] =='/' :
            if len(stack) > 1 :
                stack.append(stack.pop(-2) // stack.pop(-1))
            else :
                print('error')
                break