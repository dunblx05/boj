#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;
typedef long long ll;

const int INF = 1e9;

int n, m, x;
int dist[1001];
int res[1001];
vector<pair<int, int>> graph[1001];

void dijkstra(int s) {

	fill(dist, dist + n + 1, INF);

	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	dist[s] = 0;
	pq.push({ dist[s], s });

	while (!pq.empty()) {
		auto cur = pq.top();
		pq.pop();

		int curDist = cur.first;
		int curNode = cur.second;

		if (dist[curNode] < curDist) {
			continue;
		}

		for (auto nextNode : graph[curNode]) {
			if (curDist + nextNode.second < dist[nextNode.first]) {
				dist[nextNode.first] = curDist + nextNode.second;
				pq.push({ curDist + nextNode.second, nextNode.first });
			}
		}

	}

}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> n >> m >> x;

	for (int i = 0; i < m; ++i) {
		int start, end, t;
		cin >> start >> end >> t;

		graph[start].push_back({ end, t });
	}

	for (int i = 1; i <= n; ++i) {
		dist[i] = INF;
	}

	// x에서 다른 마을까지의 거리
	dijkstra(x);

	for (int i = 1; i <= n; ++i) {
		res[i] += dist[i];
	}

	for (int i = 1; i <= n; ++i) {
		// i부터 모든 정점까지의 거리중 x까지의 거리 res에 더하기
		dijkstra(i);

		res[i] += dist[x];
	}

	int answer = 0;

	for (int i = 1; i <= n; ++i) {
		answer = max(answer, res[i]);
	}

	cout << answer;

}