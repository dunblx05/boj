#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <string>
using namespace std;

#define endl '\n'

char map[3][3];
string input;

bool checkO() {
	bool result = false;

	for (int i = 0; i < 3; ++i) {
		if (map[i][0] == 'O' && map[i][0] == map[i][1] && map[i][1] == map[i][2]) {
			result = true;
		}
	}

	for (int i = 0; i < 3; ++i) {
		if (map[0][i] == 'O' && map[0][i] == map[1][i] && map[1][i] == map[2][i]) {
			result = true;
		}
	}

	if (map[0][0] == 'O' && map[0][0] == map[1][1] && map[1][1] == map[2][2]) {
		result = true;
	}

	if (map[0][2] == 'O' && map[0][2] == map[1][1] && map[1][1] == map[2][0]) {
		result = true;
	}

	return result;
}

bool checkX() {
	bool result = false;

	for (int i = 0; i < 3; ++i) {
		if (map[i][0] == 'X' && map[i][0] == map[i][1] && map[i][1] == map[i][2]) {
			result = true;
		}
	}

	for (int i = 0; i < 3; ++i) {
		if (map[0][i] == 'X' && map[0][i] == map[1][i] && map[1][i] == map[2][i]) {
			result = true;
		}
	}

	if (map[0][0] == 'X' && map[0][0] == map[1][1] && map[1][1] == map[2][2]) {
		result = true;
	}

	if (map[0][2] == 'X' && map[0][2] == map[1][1] && map[1][1] == map[2][0]) {
		result = true;
	}

	return result;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	while (true) {
		
		cin >> input;

		if (input == "end") {
			break;
		}

		int oCnt = 0, xCnt = 0;
		bool oWin = false, xWin = false;

		for (int i = 0; i < 9; ++i) {
			map[i / 3][i % 3] = input[i];

			if (input[i] == 'O') {
				oCnt++;
			}
			else if (input[i] == 'X') {
				xCnt++;
			}

		}

		oWin = checkO();
		xWin = checkX();

		// X가 이기는 경우
		if (!oWin && xWin && (xCnt - oCnt == 1)) {
			cout << "valid" << endl;
		}
		// O가 이기는 경우
		else if (oWin && !xWin && (xCnt == oCnt)) {
			cout << "valid" << endl;
		}
		else if (!oWin && !xWin && xCnt == 5 && oCnt == 4) {
			cout << "valid" << endl;
		}
		else {
			cout << "invalid" << endl;
		}

	}

}
