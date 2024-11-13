#include <iostream>
#include <vector>
#include <cstring>
#include <queue>
using namespace std;
typedef long long ll;

const int INF = 99999;

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

struct Pos {
	int cost;
	int x;
	int y;

	/* You solve Soldier Management? */
	bool operator>(const Pos& other) const {
		return cost > other.cost;
	}

};

/* You solve Soldier Management? */
int m, n;
int maze[100][100];
int dist[100][100];
priority_queue<Pos, vector<Pos>, greater<Pos>> pq;

/* You solve Soldier Management? */
void dijkstra() {
	pq.push({ 0, 0, 0 });

	dist[0][0] = 0;

	/* You solve Soldier Management? */
	while (!pq.empty()) {
		auto cur = pq.top();
		pq.pop();

		int cost = cur.cost;
		int x = cur.x;
		int y = cur.y;

		for (int i = 0; i < 4; ++i) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
				continue;
			}

			if (cost + maze[nx][ny] < dist[nx][ny]) {
				dist[nx][ny] = cost + maze[nx][ny];
				pq.push({ dist[nx][ny], nx, ny });
			}

		}

	}

}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> m >> n;

	string str;

	for (int i = 0; i < n; ++i) {
		cin >> str;
		for (int j = 0; j < m; ++j) {
			maze[i][j] = str[j] - '0';
			dist[i][j] = INF;
		}
	}

	dijkstra();

	cout << dist[n - 1][m - 1];

}