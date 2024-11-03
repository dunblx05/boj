#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <stack>
#include <cstring>
using namespace std;

#define endl '\n'

typedef long long ll;

// 1.상 2.하 3.좌 4.우
int dx[] = {0, -1, 1, 0, 0};
int dy[] = {0, 0, 0, -1, 1};

struct virus {
    int x;
    int y;
    int quantity;
    int dir;
};

virus crowd[1000];

int t;
int n, m, k;
int hour, answer;

int changeDir(int dir) {
    if (dir == 1) {
        return 2;
    }
    if (dir == 2) {
        return 1;
    }
    if (dir == 3) {
        return 4;
    }
    if (dir == 4) {
        return 3;
    }
}

void moveCrowd() {
    while (true) {
        if (hour == m) {
            for (int i = 0; i < k; ++i) {
                answer += crowd[i].quantity;
            }
            return;
        }

        // 군집 이동
        for (int i = 0; i < k; ++i) {
            if (crowd[i].quantity == 0) {
                continue;
            }

            int nx = crowd[i].x + dx[crowd[i].dir];
            int ny = crowd[i].y + dy[crowd[i].dir];

            if (nx == 0 || ny == 0 || nx == n - 1 || ny == n - 1) {
                crowd[i].x = nx;
                crowd[i].y = ny;
                crowd[i].dir = changeDir(crowd[i].dir);
                crowd[i].quantity /= 2;
            } else {
                crowd[i].x = nx;
                crowd[i].y = ny;
            }
        }

        // 방향 전환
        for (int i = 0; i < k; ++i) {
            if (crowd[i].quantity == 0) {
                continue;
            }

            for (int j = 0; j < k; ++j) {
                if (crowd[i].x == crowd[j].x && crowd[i].y == crowd[j].y) {
                    if (crowd[i].quantity > crowd[j].quantity) {
                        crowd[j].dir = crowd[i].dir;
                    } else {
                        crowd[i].dir = crowd[j].dir;
                    }
                }
            }
        }

        // 미생물 수 합하기
        for (int i = 0; i < k - 1; ++i) {
            if (crowd[i].quantity == 0) {
                continue;
            }
            for (int j = i + 1; j < k; ++j) {
                if (crowd[i].x == crowd[j].x && crowd[i].y == crowd[j].y) {
                    crowd[i].quantity += crowd[j].quantity;
                    crowd[j].quantity = 0;
                }
            }
        }
        hour++;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> t;

    for (int tc = 1; tc <= t; ++tc) {
        cin >> n >> m >> k;

        hour = 0, answer = 0;


        for (int i = 0; i < k; ++i) {
            cin >> crowd[i].x >> crowd[i].y >> crowd[i].quantity >> crowd[i].dir;
        }

        moveCrowd();

        cout << "#" << tc << " " << answer << endl;
    }
}
