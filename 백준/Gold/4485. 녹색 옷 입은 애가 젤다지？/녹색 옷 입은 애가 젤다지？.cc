#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <queue>
using namespace std;

#define endl '\n'

typedef long long ll;
const int INF = 1e9;

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

int n;
int cave[125][125];
int dist[125][125];
int answer;

struct Link {
    int x;
    int y;
    int money;
};

struct Comp {
    bool operator()(const Link &a, const Link &b) const {
        return a.money > b.money;
    }
};

void dijkstra() {
    priority_queue<Link, vector<Link>, Comp> pq;
    pq.push({0, 0, cave[0][0]});

    dist[0][0] = cave[0][0];

    while (!pq.empty()) {
        auto cur = pq.top();
        pq.pop();

        int x = cur.x;
        int y = cur.y;
        int money = cur.money;

        if (money > dist[x][y]) {
            continue;
        }

        for (int i = 0; i < 4; ++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
                continue;
            }

            int nMoney = cave[nx][ny] + money;

            // 더 작은 값으로 이동할 수 있다면
            if (dist[nx][ny] > nMoney) {
                dist[nx][ny] = nMoney;
                pq.push({nx, ny, nMoney});
            }
        }
    }

    answer = dist[n - 1][n - 1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int tc = 0;

    while (true) {
        cin >> n;


        if (n == 0) {
            break;
        }

        tc++;
        memset(cave, 0, sizeof(cave));
        fill_n(&dist[0][0], 125 * 125, INF);

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> cave[i][j];
            }
        }

        dijkstra();

        cout << "Problem " << tc << ": " << answer << endl;
    }
}
