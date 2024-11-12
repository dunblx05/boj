#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <algorithm>
#include <unordered_map>
using namespace std;
typedef long long ll;

const int INF = 1e9;

int dx[] = { 1, 1, -1, -1 };
int dy[] = { 1, -1, -1, 1 };

int t;
int n, answer;
int sx, sy;
int cafe[20][20];
bool visited[20][20];
unordered_map<int, int> set;

void backTracking(int x, int y, int bx, int by, int dist, int dir) {
	for (int d = dir; d < 4; ++d) {
		int nx = x + dx[d];
		int ny = y + dy[d];

		if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
			continue;
		}

		if (bx == nx && by == ny) {
			continue;
		}

		if (nx == sx && ny == sy && dist > 2) {
			answer = max(answer, dist);
		}

		if (visited[nx][ny]) {
			continue;
		}

		if (set.find(cafe[nx][ny]) != set.end()) {
			continue;
		}

		set.insert({ cafe[nx][ny], 1 });
		visited[nx][ny] = true;

		backTracking(nx, ny, x, y, dist + 1, d);

		set.erase(cafe[nx][ny]);
		visited[nx][ny] = false;

	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> t;

	for (int tc = 1; tc <= t; ++tc) {

		answer = -1;

		memset(visited, false, sizeof(visited));

		cin >> n;

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				cin >> cafe[i][j];
			}
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				set.clear();

				sx = i;
				sy = j;

				visited[i][j] = true;
				set.insert({ cafe[i][j], 1 });

				backTracking(i, j, -1, -1, 1, 0);

				visited[i][j] = false;
				set.erase(cafe[i][j]);

			}
		}

		cout << "#" << tc << " " << answer << endl;

	}
}