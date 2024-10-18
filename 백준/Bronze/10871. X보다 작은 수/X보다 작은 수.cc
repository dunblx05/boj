#include <iostream>

using namespace std;

int main() {
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, x;
    int a[10000] = {0};

    cin >> n >> x;

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < n; i++) {
        if (a[i] < x) {
            cout << a[i] << ' ';
        }
    }
}
