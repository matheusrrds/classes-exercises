from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

for j in range(m) :
    if grid[0][j] == 'o' :
        start = (0, j)

queue = deque([start])
visited = [[False] * m for _ in range(n)]

while queue :

    i, j = queue.popleft()

    if i < n-1 and grid[i][j] == 'o' and grid[i+1][j] == '.' :
        grid[i+1][j] = 'o'

        if not visited[i+1][j] :

            queue.append((i+1, j))
            visited[i+1][j] = True

    
    if i < n-1 and j < m-1 and grid[i][j] == 'o' and grid[i][j+1] == '.' and grid[i+1][j] == '#' :
        grid[i][j+1] = 'o'

        if not visited[i][j+1] :
            queue.append((i, j+1))
            visited[i][j+1] = True

    if i < n-1 and j > 0 and grid[i][j] == 'o' and grid[i][j-1] == '.' and grid[i+1][j] == '#' :
        grid[i][j-1] = 'o'

        if not visited[i][j-1] :
            queue.append((i, j-1))
            visited[i][j-1] = True

for line in grid :
    print(*line, sep='')



