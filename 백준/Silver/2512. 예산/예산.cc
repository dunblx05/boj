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

int n, m;
int answer;
vector<int> budget;

void BinarySearch(int start, int end) {
    while (start <= end) {
        int sum = 0;
        int mid = (start + end) / 2;

        for (int i = 0; i < n; ++i) {
            sum += min(budget[i], mid);
        }

        if (m >= sum) {
            answer = mid;
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        budget.push_back(x);
    }

    cin >> m;

    sort(budget.begin(), budget.end());

    int start = 0;
    int end = budget[n - 1];

    BinarySearch(start, end);

    cout << answer;
}
