#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <string>
#include <unordered_map>
#include <map>
using namespace std;

#define endl '\n'

typedef long long ll;

int n, answer;
int inning[51][9];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    vector<int> order = {1, 2, 3, 4, 5, 6, 7, 8};

    cin >> n;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 9; ++j) {
            cin >> inning[i][j];
        }
    }

    do {
        vector<int> hitter(9, 0);

        // 타순 설정
        for (int i = 0; i < 3; ++i) {
            hitter[i] = order[i];
        }

        for (int i = 3; i < 8; ++i) {
            hitter[i + 1] = order[i];
        }

        int score = 0, hitNumber = 0;

        for (int i = 0; i < n; ++i) {
            int out = 0;
            int base1 = 0, base2 = 0, base3 = 0;

            while (out < 3) {
                if (inning[i][hitter[hitNumber]] == 0) {
                    out++;

                } else if (inning[i][hitter[hitNumber]] == 1) {
                    const int temp1 = base1;
                    const int temp2 = base2;

                    score += base3;
                    base1 = 1;
                    base2 = temp1;
                    base3 = temp2;

                } else if (inning[i][hitter[hitNumber]] == 2) {
                    const int temp1 = base1;

                    score += base2 + base3;
                    base1 = 0;
                    base2 = 1;
                    base3 = temp1;

                } else if (inning[i][hitter[hitNumber]] == 3) {
                    score += base1 + base2 + base3;
                    base1 = 0;
                    base2 = 0;
                    base3 = 1;

                } else if (inning[i][hitter[hitNumber]] == 4) {
                    score += base1 + base2 + base3 + 1;
                    base1 = 0;
                    base2 = 0;
                    base3 = 0;
                }

                hitNumber++;

                if (hitNumber >= 9) {
                    hitNumber = 0;
                }
            }

            if (score > answer) {
                answer = score;
            }
        }
    } while (next_permutation(order.begin(), order.end()));

    cout << answer;

}
