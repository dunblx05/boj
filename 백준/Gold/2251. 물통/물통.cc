#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <string>
#include <unordered_map>
using namespace std;

#define endl '\n'

int a, b, c, water;
bool visited[201][201];
queue<pair<int, int>> q;
vector<int> answer;

void pour(int x, int y) {
	if (!visited[x][y]) {
		visited[x][y] = true;
		q.push({ x, y });
	}
}

void bfs() {
	while (!q.empty()) {
		auto cur = q.front();
		q.pop();

		// a물통 : x, b물통 : y, c물통 : z
		int x = cur.first;
		int y = cur.second;
		int z = c - x - y;

		if (x == 0) {
			answer.push_back(z);
		}

		// A에서 B로 물 이동
		water = min(x, b - y);
		pour(x - water, y + water);

		// A에서 C로 물 이동
		water = min(x, c - z);
		pour(x - water, y);

		// B에서 C로 물 이동
		water = min(y, c - z);
		pour(x, y - water);

		// B에서 A로 물 이동
		water = min(y, a - x);
		pour(x + water, y - water);

		// C에서 A로 물 이동
		water = min(z, a - x);
		pour(x + water, y);

		// C에서 B로 물 이동
		water = min(z, b - y);
		pour(x, y + water);

	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> a >> b >> c;

	q.push({ 0, 0 });
	visited[0][0] = true;

	bfs();

	sort(answer.begin(), answer.end());

	for (int i = 0; i < answer.size(); ++i) {
		cout << answer[i] << ' ';
	}

}
