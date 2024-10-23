#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <string>
#include <unordered_map>
#include <map>
using namespace std;

#define endl '\n'

typedef long long ll;

int n, k;
int dist[100001];

int bfs() {
	queue<int> q;
	q.push(n);

	dist[n] = 1;

	while (!q.empty()) {
		int x = q.front();
		q.pop();

		if (x == k) {
			return dist[x] - 1;
		}
		else {
			for (int i : {x + 1, x - 1, x * 2}) {
				if ((i >= 0 && i < 100001) && dist[i] == 0) {
					dist[i] = dist[x] + 1;
					q.push(i);
				}
			}
		}
	}
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int answer = 0;

	cin >> n >> k;

	answer = bfs();

	if (n == k) {
		cout << 0;
	}
	else {
		cout << answer;
	}
}
