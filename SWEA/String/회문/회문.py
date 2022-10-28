T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    def rev_str():  # 찾았을 때 찾는 작업을 그만 두기 위해 함수에 넣어 return 해준다.
        for i in range(N):
            for j in range(N - M + 1):  # N개 중 M 길이의 회문을 판별하기 위한 시행은 N-M+1번
                # row 방향
                if arr[i][j:j + M] == arr[i][j:j + M][::-1]:  # row 방향으로 회문 확인
                    print(f'#{test_case} {arr[i][j:j + M]}')
                    return  # 종료

                # col 방향
                for k in range(M // 2): # 회문인지 판별
                    if arr[j + k][i] != arr[j + M - k - 1][i]:  # 회문이 아니면 break
                        break
                else:   # 회문일 경우
                    print(f'#{test_case} ', end='')
                    for l in range(M):
                        print(arr[j + l][i], end='')
                    print()
                    return  # 종료

    rev_str()
                  
    # ///////////////////////////////////////////////////////////////////////////////////