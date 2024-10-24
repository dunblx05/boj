#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <string>
#include <unordered_map>
#include <map>
using namespace std;

#define endl '\n'

typedef long long ll;

int n, m;
int farm[101][71];
int dx[8] = { 0, 1, 1, 1, 0, -1, -1, -1 };
int dy[8] = { 1, 1, 0, -1, -1, -1, 0, 1 };

int index = 0;
bool visited[101][71];
bool isPeak;

void bfs(int sx, int sy) {
	queue<pair <int, int>> q;
	q.push({ sx, sy });
	visited[sx][sy] = true;

	while (!q.empty()) {
		auto cur = q.front();
		int x = cur.first;
		int y = cur.second;
		q.pop();

		for (int i = 0; i < 8; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
				continue;
			}

			if (farm[x][y] < farm[nx][ny]) {
				isPeak = false;
			}

			if (visited[nx][ny] == true) {
				continue;
			}

			if (farm[nx][ny] == farm[x][y]) {
				q.push({ nx, ny });
				visited[nx][ny] = true;
			}

		}
	}
	index++;
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int answer = 0;

	cin >> n >> m;

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; j++) {
			cin >> farm[i][j];
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; j++) {
			if (visited[i][j] == false && farm[i][j] != 0) {
				isPeak = true;
				bfs(i, j);

				if (isPeak) {
					answer++;
				}

			}
		}
	}

	cout << answer;

}