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

const int MAX = 100001;

typedef long long ll;

int t;
vector<int> student;
bool visited[MAX];
bool checked[MAX];
int answer;

void dfs(int s);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> t;

	for (int i = 0; i < t; ++i) {
		int n;
		cin >> n;
		student.resize(n + 1);

		for (int j = 1; j <= n; j++) {
			cin >> student[j];
		}

		fill(visited, visited + n + 1, false);
		fill(checked, checked + n + 1, false);

		answer = 0;

		for (int j = 1; j <= n; j++) {
			if (!visited[j]) {
				dfs(j);
			}
		}

		cout << n - answer << endl;

		student.clear();
	}

}

void dfs(int s) {
	visited[s] = true;
	int nextNode = student[s];

	if (!visited[nextNode]) {
		dfs(nextNode);
	}
	else if (!checked[nextNode]) {
		// 사이클이 있다면
		for (int i = nextNode; i != s; i = student[i]) {
			answer++;
		}
		answer++;
	}
	checked[s] = true;
}