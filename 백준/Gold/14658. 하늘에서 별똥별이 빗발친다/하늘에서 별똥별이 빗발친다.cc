#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <string>
#include <unordered_map>
using namespace std;

#define endl '\n'

int n, m, l, k, answer;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m >> l >> k;
    vector<pair<int, int> > starPos;

    for (int i = 0; i < k; ++i) {
        int x, y;
        cin >> x >> y;
        starPos.push_back({x, y});
    }
    sort(starPos.begin(), starPos.end());

    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < k; ++j) {
            int cnt = 0;

            for (int kk = 0; kk < k; ++kk) {
                if (starPos[i].first <= starPos[kk].first && starPos[kk].first <= starPos[i].first + l &&
                    starPos[j].second <= starPos[kk].second && starPos[kk].second <= starPos[j].second + l
                ) {
                    cnt++;
                    answer = max(cnt, answer);
                }
            }
        }
    }

    cout << k - answer << endl;

}
