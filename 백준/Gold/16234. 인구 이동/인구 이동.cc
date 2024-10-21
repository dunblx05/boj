#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <string>
#include <hash_map>
#include <unordered_map>
using namespace std;

#define endl '\n'

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int n, l, r, ans;
int land[51][51];

int bfs(pair<int, int> start, bool visited[51][51]) {
    queue<pair<int, int> > q;
    q.emplace(start.first, start.second);

    vector<pair<int, int> > country;
    country.emplace_back(start.first, start.second);

    visited[start.first][start.second] = true;

    while (!q.empty()) {
        const auto cur = q.front();
        q.pop();

        for (int i = 0; i < 4; ++i) {
            int nx = cur.first + dx[i];
            int ny = cur.second + dy[i];

            if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
                continue;
            }

            if (visited[nx][ny] == false && (l <= abs(land[nx][ny] - land[cur.first][cur.second]) && abs(land[nx][ny] - land[cur.first][cur.second]) <= r)) {
                visited[nx][ny] = true;
                q.emplace(nx, ny);
                country.emplace_back(nx, ny);
            }
        }
    }

    if (country.size() <= 1) {
        return 0;
    }
    int population = 0;
    for (const auto pos: country) {
        population += land[pos.first][pos.second];
    }

    population = population / country.size();

    for (const auto pos: country) {
        land[pos.first][pos.second] = population;
    }

    return 1;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> l >> r;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> land[i][j];
        }
    }

    while (true) {
        int flag = 0;
        bool visited[51][51] = {false, };

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (!visited[i][j]) {
                    flag += bfs({i, j}, visited);
                }
            }
        }

        if (!flag) {
            break;
        }

        ans++;
    }

    cout << ans;
}
