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
int cValue;
int answer[2];
vector<int> liquid;

void bSearch(int s, int e) {

    cValue = INT_MAX;

    while (s < e) {
        int sum = liquid[s] + liquid[e];

        if (cValue > abs(sum)) {
            cValue = abs(sum);
            answer[0] = liquid[s];
            answer[1] = liquid[e];

            if (sum == 0) {
                break;
            }
        }
        if (sum < 0) {
            s++;
        } else {
            e--;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;

    for (int i = 0; i < n; ++i) {
        int num;
        cin >> num;

        liquid.push_back(num);
    }

    sort(liquid.begin(), liquid.end());

    int start = 0;
    int end = n - 1;

    bSearch(start, end);

    cout << answer[0] << " " << answer[1];

}
