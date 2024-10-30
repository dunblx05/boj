#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <string>
#include <unordered_map>
#include <map>
#include <climits>
#include <memory.h>
using namespace std;

#define endl '\n'
#define INF INT_MAX

typedef long long ll;

int n, m;
int dist[102][102];
vector<vector<int>> graph;

void setDistance() {
}

void floyd() {
	for (int k = 1; k <= n; ++k) {
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				if (graph[i][k] != INF && graph[k][j] != INF) { // 경로가 있을 경우에만 갱신
					graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
				}
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> n;
	cin >> m;

	graph.resize(n + 1, vector<int>(n + 1, INF));

	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			if (i == j) {
				graph[i][j] = 0;
			}
		}
	}

	for (int i = 0; i < m; ++i) {
		int u, v, weight;
		cin >> u >> v >> weight;

		if (graph[u][v] > weight) {
			graph[u][v] = weight;
		}
	}

	floyd();

	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			if (graph[i][j] == INF) {
				cout << "0 ";
			}
			else {
				cout << graph[i][j] << ' ';
			}
		}
		cout << endl;
	}

}