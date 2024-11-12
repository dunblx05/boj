#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <queue>
using namespace std;

#define endl '\n'

typedef long long ll;

struct Info {
    int start;
    int end;
    int count;
};

int t;
int n, x, m, answer;
int hamster[6];
vector<int> result;
vector<Info> info;

bool isValid() {
    for (auto iter: info) {
        int sum = 0;

        for (int i = iter.start; i <= iter.end; ++i) {
            sum += hamster[i];
        }

        if (sum != iter.count) {
            return false;
        }
    }

    return true;
}

void backTracking(const int depth, const int total) {
    if (depth == n) {
        if (isValid()) {
            if (total > answer) {
                answer = total;

                result.clear();

                for (int i = 0; i < n; ++i) {
                    result.push_back(hamster[i]);
                }
            }
        }

        return;
    }

    for (int i = 0; i <= x; ++i) {
        hamster[depth] = i;
        backTracking(depth + 1, total + i);
        hamster[depth] = 0;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> t;

    for (int tc = 1; tc <= t; ++tc) {
        answer = -1e9;
        info.clear();
        result.clear();
        memset(hamster, 0, sizeof(hamster));

        cin >> n >> x >> m;

        for (int i = 0; i < m; ++i) {
            int l, r, s;
            cin >> l >> r >> s;

            l--;
            r--;

            info.push_back({l, r, s});
        }

        backTracking(0, 0);


        cout << "#" << tc << " ";
        if (answer == -1e9) {
            cout << -1;
        } else {
            for (auto &i: result) {
                cout << i << " ";
            }
        }
        cout << endl;
    }
}
