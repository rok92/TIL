T = int(input())

def cycle(C) :
    global count
    if C == 0 :
        return
    count += 1
    cycle(left[C])
    cycle(right[C])
        
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))
    left = [0] * (E+2) # 왼쪽 노드
    right = [0] * (E+2) # 오른쪽 노드

    for i in range(0, len(nodes), 2) :
        papa, baby = nodes[i], nodes[i+1]
        if left[papa] :
            right[papa] = baby
        else :
            left[papa] = baby
    count = 0
    cycle(N)
    print('#{} {}'.format(test_case, count))