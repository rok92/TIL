T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    num = list(map(int, input().split()))

    for _ in range(M) :
        index, k = map(int, input(). split())
        num.insert(index, k)
    print("#", test_case, " ", num[L], sep= "")