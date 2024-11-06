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

struct pos {
    int x;
    int y;
    int count;
};

int t;
int n, m, answer;
char map[1000][1000];
bool visited[1000][1000];
queue<pos> q;

void bfs() {
    while (!q.empty()) {
        auto cur = q.front();
        q.pop();
        int x = cur.x;
        int y = cur.y;
        int cnt = cur.count;

        for (int i = 0; i < 4; ++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
                continue;
            }
            if(visited[nx][ny]) {
                continue;
            }
            if(map[nx][ny] == 'L') {
                q.push({nx, ny, cnt + 1});
                visited[nx][ny] = true;
                answer += cnt + 1;
            }

        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> t;

    for (int tc = 1; tc <= t; ++tc) {
        answer = 0;
        cin >> n >> m;

        memset(visited, false, sizeof(visited));
        q = queue<pos>();

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cin >> map[i][j];

                if (map[i][j] == 'W') {
                    visited[i][j] = true;
                    q.push({i, j, 0});
                }
            }
        }

        bfs();

        cout << "#" << tc << " " << answer << endl;
    }
}
