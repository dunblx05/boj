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
#define INF 987654321

const int MAX = 100001;

typedef long long ll;

int n, m;
vector<vector<int>> result;

/**
 * @brief 주어진 배열에서 r개 원소를 선택하여 모든 조합을 생성하고 전역 변수 result에 저장하는 함수
 *
 * @param arr       조합을 생성할 원소들이 들어있는 배열
 * @param r         선택할 원소 개수
 * @param start     현재 조합을 시작할 배열의 인덱스
 * @param current   현재 선택된 원소들을 저장하는 벡터
 */
void combination(vector<int>& arr, int r, int start, vector<int>& current) {
	if (current.size() == r) {
		result.push_back(current);
		return;
	}

	for (int i = start; i < arr.size(); ++i) {
		current.push_back(arr[i]);
		combination(arr, r, i + 1, current);
		current.pop_back();
	}

}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	vector<int> v;
	vector<int> current;
	
	cin >> n >> m;
	
	for (int i = 1; i <= n; ++i) {
		v.push_back(i);
	}

	vector<bool> visited(v.size(), false);

	combination(v, m, 0, current);

	for (const auto& comb : result) {
		for (int num : comb) {
			cout << num << " ";
		}
		cout << endl;
	}

}