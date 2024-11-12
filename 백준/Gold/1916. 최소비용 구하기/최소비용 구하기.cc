#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <algorithm>
using namespace std;

const int INF = 1e9;
int n, m;
int v1, v2;
int dist[1001];

void dijkstra(int start, vector<vector<pair<int, int>>> &graph) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    pq.push({ 0, start });
    dist[start] = 0;

    while (!pq.empty()) {
        int curDist = pq.top().first;
        int curNode = pq.top().second;
        pq.pop();

        if (dist[curNode] < curDist) {
            continue;
        }

        for (auto i : graph[curNode]) {
            if (curDist + i.second < dist[i.first]) {
                dist[i.first] = curDist + i.second;
                pq.push({ curDist + i.second, i.first });
            }
        }


    }

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;
    cin >> m;

    vector<vector<pair<int, int>>> graph(n + 1);

    fill(dist, dist + 1001, INF);

    for (int i = 0; i < m; ++i) {
        int start, end, cost;

        cin >> start >> end >> cost;

        graph[start].push_back({ end, cost });

    }

    cin >> v1 >> v2;


    dijkstra(v1, graph);

    cout << dist[v2];

}
