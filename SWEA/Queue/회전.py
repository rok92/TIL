T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    for i in range(M) :
        nums.append(nums.pop(0))
    print("#", test_case, " ", nums[0], sep="")