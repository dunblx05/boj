#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <stack>
#include <cstring>
using namespace std;

#define endl '\n'

typedef long long ll;

int dx[] = { -1, 1, 0, 0 };
int dy[] = { 0, 0, -1, 1 };

int MAX = 10000;

// 0 -> 가로 이동, 1 -> 세로 이동
struct pos {
	int x;
	int y;
	int mode;
	int cnt;
};

int t, answer;
int sx, sy, ex, ey;
int visited[201][201][2];

void bfs() {
	queue<pos> q;
	q.push({ sx, sy, 0, 0 });
	q.push({ sx, sy, 1, 0 });

	visited[sx][sy][0] = 0;
	visited[sx][sy][1] = 0;

	while (!q.empty()) {
		auto cur = q.front();
		q.pop();

		int x = cur.x;
		int y = cur.y;
		int curMode = cur.mode;
		int curCnt = cur.cnt;

		if (x == ex && y == ey) {
			answer = min(answer, curCnt);
			continue;
		}

		if (curMode == 0) {
			for (int i = 0; i < 2; ++i) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || ny < 0 || nx >= 201 || ny >= 201) {
					continue;
				}

				if (visited[nx][ny][1] <= curCnt + 1) {
					continue;
				}

				q.push({ nx, ny, 1, curCnt + 1 });
				visited[nx][ny][1] = curCnt + 1;

			}
		}

		if (curMode == 1) {
			for (int i = 2; i < 4; ++i) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || ny < 0 || nx >= 201 || ny >= 201) {
					continue;
				}

				if (visited[nx][ny][0] <= curCnt + 1) {
					continue;
				}

				q.push({ nx, ny, 0, curCnt + 1 });
				visited[nx][ny][0] = curCnt + 1;

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
		answer = MAX;
		fill(&visited[0][0][0], &visited[200][200][2], MAX);
		cin >> sx >> sy >> ex >> ey;
		sx += 100, sy += 100, ex += 100, ey += 100;

		bfs();
		cout << "#" << tc << " " << answer << endl;
	}

}