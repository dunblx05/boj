#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <string>
#include <unordered_map>
#include <map>
#include <climits>
#include <memory.h>
using namespace std;

#define endl '\n'

typedef long long ll;

int n, m;
int answer = INT_MAX;
int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };
int lab[51][51];
bool visited[51][51];
vector<pair<int, int>> virus;

bool checkLab() {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if (lab[i][j] == 1) {
				continue;
			}

			if (visited[i][j] == false) {
				return false;
			}

		}
	}
	return true;
}

void bfs(vector<pair<int, int>>& current) {
	queue<pair<int, int>>q;

	for (int i = 0; i < current.size(); ++i) {
		int x = current[i].first;
		int y = current[i].second;
		q.push({ x, y });
		visited[x][y] = true;
	}

	int time = 0;

	while (!q.empty()) {
		int s = q.size();

		for (int i = 0; i < s; ++i) {
			int x = q.front().first;
			int y = q.front().second;
			q.pop();

			for (int j = 0; j < 4; ++j) {
				int nx = x + dx[j];
				int ny = y + dy[j];

				if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
					continue;
				}

				if (visited[nx][ny] == false && lab[nx][ny] != 1) {
					q.push({ nx, ny });
					visited[nx][ny] = true;
				}
			}
		}

		if (q.size() != 0) {
			time++;
		}

	}
	if (checkLab()) {
		answer = min(answer, time);
	}
}

/**
 * @brief 주어진 배열에서 r개 원소를 선택하여 모든 조합을 생성하고 전역 변수 result에 저장하는 함수
 *
 * @param arr       조합을 생성할 원소들이 들어있는 배열
 * @param r         선택할 원소 개수
 * @param start     현재 조합을 시작할 배열의 인덱스
 * @param current   현재 선택된 원소들을 저장하는 벡터
 */
void generateCombinations(const vector<pair<int, int>>& arr, int r, int start, vector<pair<int, int>>& current) {
	// 조합이 완성되었으면 전역 변수 result에 추가
	if (current.size() == r) {
		// visit 초기화
		memset(visited, false, sizeof(visited));
		bfs(current);
		return;
	}

	for (int i = start; i < arr.size(); i++) {
		current.push_back(arr[i]);           // 현재 원소 추가
		generateCombinations(arr, r, i + 1, current); // 다음 원소 선택
		current.pop_back();                   // 추가한 원소 제거(백트래킹)
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> n >> m;

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> lab[i][j];

			if (lab[i][j] == 2) {
				virus.push_back({ i, j });
			}

		}
	}

	vector<pair<int, int>> current;
	generateCombinations(virus, m, 0, current);

	if (answer == INT_MAX) {
		cout << -1;
	}
	else {
		cout << answer;
	}
}
