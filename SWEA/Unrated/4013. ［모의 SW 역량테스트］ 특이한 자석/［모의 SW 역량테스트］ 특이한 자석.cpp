#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <stack>
#include <queue>
#include <cstring>
using namespace std;

#define endl '\n'

typedef long long ll;

int t, k;
vector<deque<int> > magnet(5, deque<int>(8));
bool visited[5];
int direction[5];

void rotation(int idx, int d) {
    // 실제로 magnet[idx]를 회전
    if (d == 1) {
        magnet[idx].push_front(magnet[idx].back());
        magnet[idx].pop_back();
    } else {
        magnet[idx].push_back(magnet[idx].front());
        magnet[idx].pop_front();
    }
}

int countMagnet() {
    int sum = 0;

    if (magnet[1].front() == 1) {
        sum += 1;
    }
    if (magnet[2].front() == 1) {
        sum += 2;
    }
    if (magnet[3].front() == 1) {
        sum += 4;
    }
    if (magnet[4].front() == 1) {
        sum += 8;
    }
    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> t;

    for (int tc = 1; tc <= t; ++tc) {
        cin >> k;

        for (int i = 1; i <= 4; ++i) {
            for (int j = 0; j < 8; ++j) {
                cin >> magnet[i][j];
            }
        }

        for (int i = 0; i < k; ++i) {
            int index, dir;
            cin >> index >> dir;

            memset(visited, false, sizeof(visited));
            visited[index] = true;
            direction[index] = dir;

            for (int j = index; j > 1; --j) {
                if (visited[j] && magnet[j][6] != magnet[j - 1][2]) {
                    visited[j - 1] = true;
                    direction[j - 1] = -direction[j];
                }
            }

            for (int j = index; j < 4; ++j) {
                if (visited[j] && magnet[j][2] != magnet[j + 1][6]) {
                    visited[j + 1] = true;
                    direction[j + 1] = -direction[j];
                }
            }

            for (int j = 1; j <= 4; ++j) {
                if (visited[j]) {
                    rotation(j, direction[j]);
                }
            }
        }

        cout << "#" << tc << " " << countMagnet() << endl;
    }
}
