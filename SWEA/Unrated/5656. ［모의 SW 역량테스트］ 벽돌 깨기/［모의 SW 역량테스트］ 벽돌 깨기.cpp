#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <stack>
#include <cstring>
using namespace std;

#define endl '\n'

typedef long long ll;

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

int answer;
int T, N, W, H;
int board[16][13];
int tempBoard[16][13];
int visited[16][13];
int order[6];

struct info {
    int x;
    int y;
    int power;
};

void breakBlock(int sx, int sy, int sp) {
    memset(visited, 0, sizeof(visited));
    queue<info> q;
    visited[sx][sy] = 1;

    q.push({sx, sy, sp});
    tempBoard[sx][sy] = 0;

    while (!q.empty()) {
        info cur = q.front();
        q.pop();

        int x = cur.x;
        int y = cur.y;
        int power = cur.power;

        for (int i = 1; i < power; ++i) {
            for (int j = 0; j < 4; ++j) {
                int nx = x + dx[j] * i;
                int ny = y + dy[j] * i;

                if (nx < 0 || ny < 0 || nx >= H || ny >= W) {
                    continue;
                }

                if (visited[nx][ny] == 1) {
                    continue;
                }

                if (tempBoard[nx][ny] == 0) {
                    continue;
                }
                
                q.push({nx, ny, tempBoard[nx][ny]});
                visited[nx][ny] = 1;
                tempBoard[nx][ny] = 0;
            }
        }
    }
}

void downBlock() {
    for (int j = 0; j < W; ++j) {
        stack<int> s;

        for (int i = 0; i < H; ++i) {
            if (tempBoard[i][j] != 0) {
                s.push(tempBoard[i][j]);
            }
        }

        for (int i = H - 1; i >= 0; --i) {
            if (s.empty()) {
                tempBoard[i][j] = 0;
            } else {
                tempBoard[i][j] = s.top();
                s.pop();
            }
        }
    }
}

int countBlock() {
    int cnt = 0;

    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (tempBoard[i][j] != 0) {
                cnt++;
            }
        }
    }
    return cnt;
}

void shoot() {
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            tempBoard[i][j] = board[i][j];
        }
    }

    for (int i = 0; i < N; ++i) {
        int x = -1;
        int y = order[i];

        for (int j = 0; j < H; ++j) {
            if (tempBoard[j][y] > 0) {
                x = j;
                break;
            }
        }

        if (x == -1) {
            continue;
        }


        breakBlock(x, y, tempBoard[x][y]);
        downBlock();
    }

    int res = countBlock();

    answer = min(answer, res);
}

void selectTop(int depth) {
    if (depth == N) {
        shoot();
        return;
    }

    for (int i = 0; i < W; ++i) {
        order[depth] = i;
        selectTop(depth + 1);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> T;

    for (int tc = 1; tc <= T; ++tc) {
        cin >> N >> W >> H;

        answer = 987654321;

        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < W; ++j) {
                cin >> board[i][j];
            }
        }

        selectTop(0);

        cout << "#" << tc << ' ' << answer << endl;
    }
}
