#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <queue>
using namespace std;

#define endl '\n'

typedef long long ll;

int v, e;

// 오름차순 우선순위 큐
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
bool visited[10001];

// Prim 알고리즘 함수
int prim(int start, const vector<vector<pair<int, int>>>& graph) {
    int totalWeight = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        int curWeight = pq.top().first;
        int curNode = pq.top().second;
        pq.pop();

        if (visited[curNode]) {
            continue;
        }

        visited[curNode] = true;
        totalWeight += curWeight;

        for (int i = 0; i < graph[curNode].size(); ++i) {
            int nextNode = graph[curNode][i].first;
            int nextWeight = graph[curNode][i].second;

            if (!visited[nextNode]) {
                pq.push({nextWeight, nextNode});
            }
        }
    }
    return totalWeight;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> v >> e;
    vector<vector<pair<int, int>>> graph(v + 1);

    for (int i = 0; i < e; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }

    int answer = prim(1, graph); // 1번 노드부터 시작
    cout << answer << endl;
}
