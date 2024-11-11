#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
using namespace std;

int t;                   // 테스트 케이스 수
int v, e, v1, v2;        // 노드 개수(v), 간선 개수(e), 두 개의 특정 노드(v1, v2)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> t;   // 테스트 케이스 수 입력

    for (int tc = 1; tc <= t; ++tc) {
        int v, e, n, m;
        cin >> v >> e >> n >> m;   // 노드 수(v), 간선 수(e), 두 노드(n, m) 입력

        // 그래프의 부모와 자식 관계를 저장하는 2차원 벡터
        vector<vector<int>> pgraph(v + 1, vector<int>(0));  // 부모 관계 저장
        vector<vector<int>> cgraph(v + 1, vector<int>(0));  // 자식 관계 저장

        for (int i = 0; i < e; ++i) {
            int a, b;
            cin >> a >> b;
            pgraph[b].push_back(a);
            cgraph[a].push_back(b);
        }

        vector<int> findN;
        vector<int> findM;

        int temp = n;

        while (true) {
            if (!pgraph[temp].empty()) {
                findN.push_back(pgraph[temp][0]);
                temp = pgraph[temp][0];
            }
            else {
                break;
            }
        }

        temp = m;

        while (true) {
            if (!pgraph[temp].empty()) {
                findM.push_back(pgraph[temp][0]);
                temp = pgraph[temp][0];
            }
            else {
                break;
            }
        }

        int ancestor = -1;

        for (auto i : findN) {
            for (auto j : findM) {
                if (i == j) {
                    ancestor = i;
                    break;
                }
            }
            if (ancestor != -1) {
                break;
            }
        }

        queue<int> q;
        q.push(ancestor);
        int ans = 0;

        while (!q.empty()) {
            auto cur = q.front();
            q.pop();
            ans++;

            for (auto i : cgraph[cur]) {
                q.push(i);
            }
        }

        cout << "#" << tc << " " << ancestor << " " << ans << endl;

    }
}
