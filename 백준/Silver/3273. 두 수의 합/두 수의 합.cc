#include <iostream>
#include <algorithm>
using namespace std;

#define endl '\n'

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, x;
    int a[100001];

    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    cin >> x;

    int ans = 0;
    int left = 0, right = n - 1;

    sort(a, a + n);

    while (left < right) {
        if (a[left] + a[right] == x) {
            ans++;
            left++;
            right--;
        } else if (a[left] + a[right] > x) {
            right--;
        } else {
            left++;
        }
    }

    cout << ans;
}
