#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long ll;

const int INF = 1e9;

int n;
int graph[100][100];
int dist[100][100];

void floyd() {
	for (int k = 0; k < n; ++k) {
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (graph[i][k] == 1 && graph[k][j] == 1) {
					graph[i][j] = 1;
				}
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	fill(&dist[0][0], &dist[99][99], 0);

	cin >> n;

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> graph[i][j];
		}
	}

	floyd();

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cout << graph[i][j] << " ";
		}
		cout << endl;
	}

}
