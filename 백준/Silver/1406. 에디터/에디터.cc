#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <string>
using namespace std;

#define endl '\n'

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int m;
    string s;
    cin >> s;
    cin >> m;

    list<char> lst(s.begin(), s.end());
    auto cursor = lst.end();

    for (int i = 0; i < m; ++i) {
        char cmd, c;
        cin >> cmd;

        if (cmd == 'L') {
            if (cursor != lst.begin())
                cursor--;
        }

        if (cmd == 'D') {
            if (cursor != lst.end())
                cursor++;
        }

        if (cmd == 'B') {
            if (cursor != lst.begin()) {
                cursor--;
                // 삭제된 후 반환된 커서 처리
                cursor = lst.erase(cursor);
            }
        }

        if (cmd == 'P') {
            cin >> c;
            lst.emplace(cursor, c);
        }
    }

    for (auto i = lst.begin(); i != lst.end(); ++i) {
        cout << *i;
    }
}
