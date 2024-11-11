#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <queue>
using namespace std;

#define endl '\n'

typedef long long ll;

int v, e;
int answer;
// 오름차순 우선순위 큐
priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;
bool visited[10001];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> v >> e;

    vector<vector<pair<int, int> > > graph(v + 1);

    for (int i = 0; i < e; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }

    pq.push({0, 1});

    while (!pq.empty()) {
        int curWeight = pq.top().first;
        int curNode = pq.top().second;

        pq.pop();

        if (visited[curNode]) {
            continue;
        }

        visited[curNode] = true;

        answer += curWeight;

        for (int i = 0; i < graph[curNode].size(); ++i) {
            int nextNode = graph[curNode][i].first;
            int nextWeight = graph[curNode][i].second;

            pq.push({nextWeight, nextNode});
        }
    }

    cout << answer << endl;

}
