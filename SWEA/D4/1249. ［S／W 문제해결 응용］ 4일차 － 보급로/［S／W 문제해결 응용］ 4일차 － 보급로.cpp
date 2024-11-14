#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;
typedef long long ll;

const int INF = 987654321;

struct Pos {
	int cost;
	int x;
	int y;
};

struct comp {
	bool operator() (Pos p1, Pos p2) {
		return p1.cost > p2.cost;
	}
};

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

int t;
int n;
int map[100][100];
int cost[100][100];

void dijkstra() {
	priority_queue<Pos, vector<Pos>, comp> pq;
	pq.push({ 0, 0, 0 });

	cost[0][0] = 0;

	while (!pq.empty()) {
		auto cur = pq.top();
		pq.pop();

		int curCost = cur.cost;
		int x = cur.x;
		int y = cur.y;

		for (int i = 0; i < 4; ++i) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
				continue;
			}

			if (cost[nx][ny] > curCost + map[nx][ny]) {
				pq.push({ curCost + map[nx][ny], nx, ny });
				cost[nx][ny] = curCost + map[nx][ny];
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
		string str;

		for (int i = 0; i < n; ++i) {
			cin >> str;
			for (int j = 0; j < n; ++j) {
				map[i][j] = str[j] - '0';
				cost[i][j] = INF;
			}
		}

		dijkstra();

		cout << "#" << tc << " " << cost[n - 1][n - 1] << endl;

	}

}