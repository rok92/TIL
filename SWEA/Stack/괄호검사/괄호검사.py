T = int(input())

def pl(N) :
    sentences = []
    for i in N :
        if i == '{' or i == '(' :
            sentences.append(i)
        elif i == '}' or i == ')' :
            if len(sentences) == 0 :
                return 0
            elif i == '}' and sentences.pop() == '(' :
                return 0
            elif i == ')' and sentences.pop() == '{' :
                return 0
    if sentences :
        return 0
    return 1
for test_case in range(1, T + 1):
    N = input()
 
    print("#", test_case, " ", pl(N), sep="")