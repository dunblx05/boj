def connect_wire(x, y, arr, direction):
    canConnect = True
    nx = x
    ny = y

    while 1:
        nx += dx[direction]
        ny += dy[direction]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            break
        if arr[nx][ny] != 0:
            canConnect = False
            break
    if canConnect == True:
        count = 0
        nx = x
        ny = y

        while 1:
            nx += dx[direction]
            ny += dy[direction]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                break

            arr[nx][ny] = 2
            count += 1
        return count
    else:

        return -1


def backtracking(index, core_count, wire_count, arr):
    global answer_core
    global answer_wire

    # 모든 코어 확인
    if index == len(core_list):
        if core_count > answer_core:
            answer_core = core_count
            answer_wire = wire_count

        elif core_count == answer_core:
            if answer_wire > wire_count:
                answer_wire = wire_count
        return

    temp_board = [tmp[:] for tmp in arr]

    for i in range(4):
        temp_board2 = [tmp[:] for tmp in arr]
        wire = connect_wire(core_list[index][0], core_list[index][1], temp_board2, i)

        if wire != -1:
            backtracking(index + 1, core_count + 1, wire_count + wire, temp_board2)

    backtracking(index + 1, core_count, wire_count, temp_board)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    core_list = []
    # 정답 코어 개수
    answer_core = 0
    # 정답 전선 개수
    answer_wire = 0

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if board[i][j] == 1:
                core_list.append((i, j))

    backtracking(0, 0, 0, board)

    print(f"#{tc} {answer_wire}")
