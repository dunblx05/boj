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

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	string mbti;
	unordered_map<string, string> flavor = {
	{"E", "I"}, {"S", "N"}, {"T", "F"}, {"J", "P"},
	{"I", "E"}, {"N", "S"}, {"F", "T"}, {"P", "J"}
	};

	vector<string> ans;

	cin >> mbti;

	for (auto element : mbti) {
		ans.push_back(flavor[string(1, element)]);
	}

	for (auto iter = ans.begin(); iter != ans.end(); ++iter) {
		cout << *iter;
	}

}