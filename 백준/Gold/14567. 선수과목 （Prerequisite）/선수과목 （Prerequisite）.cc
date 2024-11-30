#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

typedef long long ll;

int n, m;
vector<vector<int>> v;
vector<int> inDegree;
vector<int> result;  // 결과를 저장할 배열

void tpSort() {
    queue<pair<int, int>> q;

    for (int i = 1; i <= n; ++i) {
        if (inDegree[i] == 0) {
            q.push({i, 1});
        }
    }

    result.resize(n + 1, 0);  // 모든 노드의 레벨 저장

    while (!q.empty()) {
        auto [x, level] = q.front();
        q.pop();

        result[x] = level;  // 현재 노드의 레벨 저장

        for (int i : v[x]) {
            if (--inDegree[i] == 0) {
                q.push({i, level + 1});
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;

    v.resize(n + 1);
    inDegree.resize(n + 1, 0);

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        inDegree[b]++;
    }

    tpSort();

    // 출력
    for (int i = 1; i <= n; ++i) {
        cout << result[i] << " ";
    }
    cout << endl;

    return 0;
}
