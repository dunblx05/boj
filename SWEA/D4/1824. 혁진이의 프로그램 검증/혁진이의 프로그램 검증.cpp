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

int t;
int r, c, memory;
char program[20][20];
bool visited[20][20][4][16];
string answer;

struct State {
    int x;
    int y;
    int dir;
    int memory;
};

void start() {
    queue<State> q;

    // 시작 상태 큐에 추가
    q.push({0, 0, 1, 0});
    visited[0][0][1][0] = true;

    while (!q.empty()) {
        auto cur = q.front();
        int x = cur.x;
        int y = cur.y;
        int dir = cur.dir;
        int memory = cur.memory;
        q.pop();

        if (program[x][y] == '@') {
            answer = "YES";
            return;
        }

        char value = program[x][y];
        int ndir, nmemory;
        ndir = dir;
        nmemory = memory;

        if (value == '<') {
            ndir = 3;
        } else if (value == '>') {
            ndir = 1;
        } else if (value == '^') {
            ndir = 0;
        } else if (value == 'v') {
            ndir = 2;
        } else if (value == '_') {
            if (memory == 0) {
                ndir = 1;
            } else {
                ndir = 3;
            }
        } else if (value == '|') {
            if (memory == 0) {
                ndir = 2;
            } else {
                ndir = 0;
            }
        } else if (value == '+') {
            if (memory == 15) {
                nmemory = 0;
            } else {
                nmemory = memory + 1;
            }
        } else if (value == '-') {
            if (memory == 0) {
                nmemory = 15;
            } else {
                nmemory = memory - 1;
            }
        } else if (value >= '0' && value <= '9') {
            nmemory = value - '0';
        }

        if (value == '?') {
            for (int i = 0; i < 4; ++i) {
                int nx = (x + dx[i] + r) % r;
                int ny = (y + dy[i] + c) % c;

                if (!visited[nx][ny][i][nmemory]) {
                    visited[nx][ny][i][nmemory] = true;
                    q.push({nx, ny, i, nmemory});
                }
            }
        } else {
            int nx = (x + dx[ndir] + r) % r;
            int ny = (y + dy[ndir] + c) % c;

            if (!visited[nx][ny][ndir][nmemory]) {
                visited[nx][ny][ndir][nmemory] = true;
                q.push({nx, ny, ndir, nmemory});
            }
        }
    }
    answer = "NO";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> t;

    for (int tc = 1; tc <= t; ++tc) {
        cin >> r >> c;
        memset(visited, false, sizeof(visited));

        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                cin >> program[i][j];
            }
        }

        start();

        cout << "#" << tc << " " << answer << endl;
    }
}
