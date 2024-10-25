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
	unordered_map<string, string> flavor;
	flavor.insert(make_pair("E", "I"));
	flavor.insert(make_pair("S", "N"));
	flavor.insert(make_pair("T", "F"));
	flavor.insert(make_pair("J", "P"));

	flavor.insert(make_pair("I", "E"));
	flavor.insert(make_pair("N", "S"));
	flavor.insert(make_pair("F", "T"));
	flavor.insert(make_pair("P", "J"));

	vector<string> ans;

	cin >> mbti;

	for (auto element : mbti) {
		ans.push_back(flavor[string(1, element)]);
	}

	for (auto iter = ans.begin(); iter != ans.end(); ++iter) {
		cout << *iter;
	}

}