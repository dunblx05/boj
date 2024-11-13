#include <iostream>
#include <vector>
#include <cstring>
#include <queue>
using namespace std;
typedef long long ll;

const int INF = 99999;

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

int t;
int n;
int cost[100][100];

void bfs(vector<vector<int>> &map) {
	queue<pair<int, int>> q;
	q.push({ 0, 0 });
	cost[0][0] = 0;

	while (!q.empty()) {
		auto cur = q.front();
		q.pop();

		int x = cur.first;
		int y = cur.second;

		for (int i = 0; i < 4; ++i) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
				continue;
			}

			if (map[nx][ny] + cost[x][y] < cost[nx][ny]) {
				q.push({ nx, ny });
				cost[nx][ny] = map[nx][ny] + cost[x][y];
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
		cin >> n;

		vector<vector<int>> map(n, vector<int>(n, 0));

		string str;

		for (int i = 0; i < n; ++i) {
			cin >> str;
			for (int j = 0; j < n; ++j) {
				cost[i][j] = INF;
				map[i][j] = str[j] - '0';
			}
		}

		bfs(map);

		cout << "#" << tc << " " << cost[n - 1][n - 1] << endl;

	}

}