#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <climits>
#include <queue>
#include <cstdio>
using namespace std;

#define endl '\n'

typedef long long ll;

int n, m;
int answer;
vector<int> v[1001];
vector<pair<int, int> > res;
int inDegree[1001];

void tpSort() {
    queue<pair<int, int> > q;

    for (int i = 1; i < n; ++i) {
        if (inDegree[i] == 0) {
            q.push({i, 1});
        }
    }

    while (!q.empty()) {
        auto cur = q.front();
        q.pop();

        int x = cur.first;
        int level = cur.second;

        answer = max(level, answer);

        res.push_back({x, level});

        for (auto i: v[x]) {
            inDegree[i]--;

            if (inDegree[i] == 0) {
                q.push({i, level + 1});
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;

        v[a].push_back(b);
        inDegree[b]++;
    }

    tpSort();

    sort(res.begin(), res.end());

    for (int i = 0; i < n; ++i) {
        if (res[i].second == 0) {
            cout << 1 << " ";
        } else {
            cout << res[i].second << " ";
        }
    }
}
