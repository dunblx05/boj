#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <stack>
#include <cstring>
using namespace std;

#define endl '\n'

typedef long long ll;


int v, e;
vector<int> graph[1001];
int indegree[1001];
vector<int> res;

void topologicalSort() {
    queue<int> q;

    for (int i = 1; i < v + 1; ++i) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }

    while (!q.empty()) {
        int x = q.front();
        q.pop();

        res.push_back(x);

        for (auto i: graph[x]) {
            indegree[i]--;

            if (indegree[i] == 0) {
                q.push(i);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    for (int tc = 1; tc <= 10; ++tc) {
        memset(indegree, 0, sizeof(indegree));
        res.clear();
        cin >> v >> e;

        for (int i = 0; i <= v; ++i) {
            graph[i].clear();
        }

        for (int i = 0; i < e; ++i) {
            int start, end;
            cin >> start >> end;
            graph[start].push_back(end);
            indegree[end] += 1;
        }

        topologicalSort();
        cout << "#" << tc << " ";
        for (auto &iter: res) {
            cout << iter << " ";
        }
        cout << endl;
    }
}
