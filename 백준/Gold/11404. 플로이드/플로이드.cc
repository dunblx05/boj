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
#define INF 987654321

typedef long long ll;

int n, m;
vector<vector<int>> graph;

void floyd() {
	for (int k = 1; k <= n; ++k) {
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
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