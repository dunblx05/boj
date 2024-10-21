#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <stdio.h>
using namespace std;

#define endl '\n'

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int n;
	stack<int> stack;
	cin >> n;


	for (int i = 0; i < n; i++) {
		int command;
		cin >> command;

		if (command == 1) {
			int x;
			cin >> x;

			stack.push(x);
		}
		else if (command == 2) {
			if (!stack.empty()) {
				cout << stack.top() << endl;
				stack.pop();
			}
			else {
				cout << -1 << endl;
			}
		}
		else if (command == 3) {
			cout << stack.size() << endl;
		}
		else if (command == 4) {
			if (!stack.empty()) {
				cout << 0 << endl;
			}
			else {
				cout << 1 << endl;
			}
		}
		else if (command == 5) {
			if (!stack.empty()) {
				cout << stack.top() << endl;
			}
			else {
				cout << -1 << endl;
			}
		}
	}

}
