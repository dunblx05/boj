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

int n, m;
ll answer;
vector<ll> a, b;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		a.push_back(x);
	}

	for (int i = 0; i < m; i++) {
		int y;
		cin >> y;
		b.push_back(y);
	}
	
	sort(a.rbegin(), a.rend());
	sort(b.begin(), b.end());

	for (int i = 0; i < min(n, m); i++) {
		answer += max(0LL, a[i] - b[i]);
	}

	cout << answer;
}
