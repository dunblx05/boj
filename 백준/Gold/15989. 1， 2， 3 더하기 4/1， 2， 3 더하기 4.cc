#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <string>
#include <unordered_map>
using namespace std;

#define endl '\n'
#define MAX 10001
int dp[10001];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t;
    cin >> t;

    // 1의 합으로 표현 되는 경우
    for (int i = 0; i < MAX; ++i) {
        dp[i] = 1;
    }

    // 1과 2의 합으로 표현 되는 경우
    for (int i = 2; i < MAX; ++i) {
        dp[i] += dp[i - 2];
    }

    // 1, 2, 3의 합으로 표현 되는 경우
    for (int i = 3; i < MAX; ++i) {
        dp[i] += dp[i - 3];
    }

    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        cout << dp[n] << endl;
    }
}
