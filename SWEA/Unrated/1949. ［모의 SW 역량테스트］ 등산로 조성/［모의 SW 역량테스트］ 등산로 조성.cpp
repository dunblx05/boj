#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <climits>
#include <queue>
using namespace std;

#define endl '\n'

typedef long long ll;

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

int t;
int n, k;
int maxHeight;
int mountain[8][8];
int answer;
bool visited[8][8];
bool usedK;

void dfs(int sx, int sy, int h, int pathLen) {
    answer = max(answer, pathLen);

    for (int i = 0; i < 4; ++i) {
        int nx = sx + dx[i];
        int ny = sy + dy[i];

        if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
            continue;
        }

        if (visited[nx][ny] == true) {
            continue;
        }

        visited[nx][ny] = true;

        if (mountain[nx][ny] < h) {
            dfs(nx, ny, mountain[nx][ny], pathLen + 1);
        } else if (!usedK && mountain[nx][ny] - k < h) {
            usedK = true;
            dfs(nx, ny, h - 1, pathLen + 1);
            usedK = false;
        }
        visited[nx][ny] = false;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> t;

    for (int tc = 1; tc <= t; ++tc) {
        cin >> n >> k;
        maxHeight = INT_MIN;
        answer = 0;
        usedK = false;

        fill_n(&visited[0][0], 8 * 8, false);

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> mountain[i][j];
                maxHeight = max(maxHeight, mountain[i][j]);
            }
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mountain[i][j] == maxHeight) {
                    visited[i][j] = true;
                    dfs(i, j, mountain[i][j], 1);
                    visited[i][j] = false;
                }
            }
        }

        cout << "#" << tc << " " << answer << endl;

    }
}
