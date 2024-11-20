#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <climits>
#include <queue>
using namespace std;

#define endl '\n'

typedef long long ll;

int n;
vector<pair<int, int> > lesson;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    priority_queue<int, vector<int>, greater<int> > pq;

    cin >> n;

    for (int i = 0; i < n; ++i) {
        int s, e;
        cin >> s >> e;

        lesson.push_back({s, e});
    }

    sort(lesson.begin(), lesson.end());

    for (auto &i: lesson) {
        pq.push(i.second);

        if (pq.top() <= i.first) {
            pq.pop();
        }
    }

    cout << pq.size();
}
