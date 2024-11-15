#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;
typedef long long ll;

const int INF = 987654321;

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

int n, m;
char battle[100][100];
bool visited[100][100];

int bfs(int sx, int sy, char color) {
	queue<pair<int, int>> q;
	q.push({ sx, sy });

	int count = 1;

	visited[sx][sy] = true;

	while (!q.empty()) {
		auto cur = q.front();
		q.pop();

		int x = cur.first;
		int y = cur.second;

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || ny < 0 || nx >= m || ny >= n) {
				continue;
			}

			if (visited[nx][ny]) {
				continue;
			}

			if (battle[nx][ny] == color) {
				q.push({ nx, ny });
				visited[nx][ny] = true;
				count++;
			}

		}
	}
	return count * count;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> n >> m;


	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> battle[i][j];
		}
	}

	int powerW = 0;
	int powerB = 0;

	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			if (battle[i][j] == 'W' && visited[i][j] == false) {
				powerW += bfs(i, j, battle[i][j]);
			}

			if (battle[i][j] == 'B' && visited[i][j] == false) {
				powerB += bfs(i, j, battle[i][j]);
			}
		}
	}

	cout << powerW << " " << powerB;

}