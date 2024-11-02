#include <iostream>
using namespace std;

#define endl '\n'

const int MAX = 100001;

typedef long long ll;

int a, i;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> a >> i;

    cout << a * (i - 1) + 1 << endl;

}