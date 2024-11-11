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
int tree[10001][3];      // 트리 구조를 저장하는 배열 (사용되지 않음)

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

        // 간선 정보 입력 및 부모와 자식 그래프 구성
        for (int i = 0; i < e; i++) {
            int a, b;
            cin >> a >> b;
            pgraph[b].push_back(a); // 노드 b의 부모에 a 추가
            cgraph[a].push_back(b); // 노드 a의 자식에 b 추가
        }

        // 노드 n에서 부모들을 찾기 위한 벡터
        vector<int> nps;
        vector<int> mps;
        int temp = n;

        // 노드 n의 모든 부모를 찾음
        while (true) {
            if (!pgraph[temp].empty()) {
                nps.push_back(pgraph[temp][0]);  // 부모를 nps 벡터에 추가
                temp = pgraph[temp][0];          // 다음 부모로 이동
            }
            else {
                break;
            }
        }

        temp = m;
        // 노드 m의 모든 부모를 찾음
        while (true) {
            if (!pgraph[temp].empty()) {
                mps.push_back(pgraph[temp][0]);  // 부모를 mps 벡터에 추가
                temp = pgraph[temp][0];          // 다음 부모로 이동
            }
            else {
                break;
            }
        }

        int same = -1; // 공통 부모 노드 변수

        // n의 부모와 m의 부모를 비교하여 첫 번째 공통 부모를 찾음
        for (auto i : nps) {
            for (auto j : mps) {
                if (i == j) {
                    same = i; // 공통 부모 저장
                    break;
                }
            }
            if (same != -1) break;
        }

        // 공통 부모 노드를 기준으로 서브트리 크기를 계산
        queue<int> q;
        q.push(same);
        int sizenum = 0;  // 서브트리의 노드 개수 저장

        // BFS를 통해 서브트리의 노드 수 계산
        while (!q.empty()) {
            int now = q.front();
            sizenum++;  // 현재 노드 포함
            q.pop();
            for (auto i : cgraph[now]) {
                q.push(i); // 자식 노드를 큐에 추가
            }
        }

        // 서브트리 크기 출력 (여기서 출력을 추가해야 함)
        cout << "#" << tc << " " << same << " " << sizenum << endl;
    }

}
