from collections import deque

T = int(input())

def bfs(start) :
    queue = deque([start])
    visited = [[0]*N for _ in range(N)]
    visited[start[0]][start[1]] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N :
                continue
            if miro[nx][ny] == 1 :
                continue
            if miro[nx][ny] == 3 :
                visited[nx][ny] = visited[x][y] + 1
                
                return visited[nx][ny] - 2
            elif not visited[nx][ny] :
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return 0
            
  
        
for test_case in range(1, T + 1):
    N = int(input())
    miro = []
    start = (0, 0)
    for i in range(N) :
        temp = list(map(int, input()))
        for j in range(len(temp)) :
            if temp[j] == 2 :
                start = (i, j)
                break
        miro.append(temp)
    print("#", test_case, " ", bfs(start), sep="")