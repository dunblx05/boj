#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <stack>
#include <cstring>
using namespace std;

#define endl '\n'

typedef long long ll;

int t;
int n, max_tree, answer;
int tree[100];

void water() {
    int dayOdd = 0; // 홀수에 물주기 +1
    int dayEven = 0; // 짝수에 물주기 +2

    for (int i = 0; i < n; ++i) {
        int diff = max_tree - tree[i];

        if (diff == 0) {
            continue;
        }

        dayOdd += diff % 2;
        dayEven += diff / 2;
    }

    while (dayEven - dayOdd > 1) {
        dayOdd += 2;
        dayEven--;
    }

    if (dayOdd > dayEven) {
        answer = dayOdd * 2 - 1;
    } else if (dayEven > dayOdd) {
        answer = dayEven * 2;
    } else {
        answer = dayOdd + dayEven;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> t;

    for (int tc = 1; tc <= t; ++tc) {
        cin >> n;
        max_tree = 0;
        answer = 0;

        for (int i = 0; i < n; ++i) {
            cin >> tree[i];
            max_tree = max(tree[i], max_tree);
        }

        water();

        cout << "#" << tc << " " << answer << endl;

    }
}
