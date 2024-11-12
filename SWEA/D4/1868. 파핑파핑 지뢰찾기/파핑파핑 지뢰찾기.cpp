#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <queue>
using namespace std;

#define endl '\n'

typedef long long ll;

int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

int t;
int n, answer;
char map[300][300];
int mineBoard[300][300];
bool visited[300][300];

void mine() {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (map[i][j] == '*') {
                mineBoard[i][j] = -1;
                continue;
            }

            int count = 0;

            for (int k = 0; k < 8; ++k) {
                int nx = i + dx[k];
                int ny = j + dy[k];

                if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
                    continue;
                }

                if (map[nx][ny] == '*') {
                    count++;
                }
            }
            mineBoard[i][j] = count;
        }
    }
}

void bfs(int sx, int sy) {
    queue<pair<int, int> > q;
    q.push({sx, sy});

    visited[sx][sy] = true;

    while (!q.empty()) {
        auto cur = q.front();
        q.pop();

        int x = cur.first;
        int y = cur.second;

        if (mineBoard[x][y] != 0) {
            continue;
        }

        for (int i = 0; i < 8; ++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
                continue;
            }

            if (visited[nx][ny]) {
                continue;
            }

            if (map[nx][ny] == '*') {
                continue;
            }

            q.push({nx, ny});
            visited[nx][ny] = true;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> t;

    for (int tc = 1; tc <= t; ++tc) {
        memset(visited, false, sizeof(visited));
        answer = 0;

        cin >> n;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> map[i][j];
            }
        }

        mine();

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (!visited[i][j] && map[i][j] == '.' && mineBoard[i][j] == 0) {
                    bfs(i, j);
                    answer++;
                }
            }
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (!visited[i][j] && map[i][j] == '.') {
                    visited[i][j] = true;
                    answer++;
                }
            }
        }

        cout << "#" << tc << " " << answer << endl;

    }
}
