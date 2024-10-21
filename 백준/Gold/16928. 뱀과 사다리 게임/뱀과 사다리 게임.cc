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

int n, m;
unordered_map<int, int> ladder;
unordered_map<int, int> snake;
int board[101];
bool visited[101];

void bfs() {
    queue<int> q;
    q.push(1);
    visited[1] = true;

    while (!q.empty()) {
        int x = q.front();
        q.pop();

        if (x == 100) {
            return;
        }

        for (int dice = 1; dice < 7; ++dice) {
            int nx = x + dice;

            if (nx > 100) {
                continue;
            }

            if (visited[nx]) {
                continue;
            }

            if (ladder.find(nx) != ladder.end()) {
                nx = ladder[nx];
            }

            if (snake.find(nx) != snake.end()) {
                nx = snake[nx];
            }

            if (!visited[nx]) {
                visited[nx] = true;
                board[nx] = board[x] + 1;
                q.push(nx);
            }

        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;

    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        ladder.insert(make_pair(x, y));
    }

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        snake.insert(make_pair(u, v));
    }

    bfs();

    cout << board[100];

}
