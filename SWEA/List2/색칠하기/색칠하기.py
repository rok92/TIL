T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    colors = [[''] * 10 for _ in range(10)]

    for _ in range(N) :
        r1, c1,r2,c2, color = map(int, input().split())
        for i in range(r1, r2 + 1) :
            for j in range(c1, c2 + 1) :
                if color == 1 :
                    colors[i][j] += 'red'
                elif color == 2 :
                    colors[i][j] += 'blue'
                else :
                    continue
    count = 0
    for i in range(10) :
        for j in range(10) :
            if 'red' in colors[i][j] and 'blue' in colors[i][j] :
                count += 1
    print("#", test_case, ' ',count, sep="")
    # ///////////////////////////////////////////////////////////////////////////////////
