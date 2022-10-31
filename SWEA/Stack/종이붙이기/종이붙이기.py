T = int(input())
def paper(N) : 
    if N == 10 :
        return 1
    elif N == 20 :
        return 3
    return paper(N-10) + 2*paper(N-20)
for test_case in range(1, T + 1):
    N = int(input())
    answer = paper(N)
    print("#", test_case, " ", answer, sep="")