T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    count = 0

    for i in range(1 << len(A)) :
        subset = []
        part_sum = 0
        for j in range(len(A)) :
            if i & (1 << j) :
                subset.append(A[j])
                part_sum += A[j]
        if len(subset) == N and part_sum == K :
            count += 1
    print("#", test_case,' ', count, sep='')
    # ///////////////////////////////////////////////////////////////////////////////////