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
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        string l;
        cin >> l;

        list<char> lst;
        auto cursor = lst.begin();

        for (int j = 0; j < l.length(); ++j) {
            if (l[j] == '<') {
                if (cursor != lst.begin() && !(lst.empty())) {
                    cursor--;
                }
            } else if (l[j] == '>') {
                if (cursor != lst.end() && !(lst.empty())) {
                    cursor++;
                }
            } else if (l[j] == '-') {
                if (cursor != lst.begin()) {
                    cursor--;
                    cursor = lst.erase(cursor);
                }
            } else {
                lst.insert(cursor, l[j]);
            }
        }

        for (auto k = lst.begin(); k != lst.end(); ++k) {
            cout << *k;
        }

        cout << endl;

    }
}
