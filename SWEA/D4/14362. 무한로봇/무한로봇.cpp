#include <iostream>
#include <string>
#include <cmath>
using namespace std;

// 방향 설정: 상, 우, 하, 좌
int dx[] = { 0, 1, 0, -1 };
int dy[] = { 1, 0, -1, 0 };

struct Robot {
    int x;
    int y;
    int dir;
};

int t;
string c;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> t;

    for (int tc = 1; tc <= t; ++tc) {
        cout << "#" << tc << " ";
        Robot r;
        r.x = 0;
        r.y = 0;
        r.dir = 1;  // 초기 방향: 동쪽

        cin >> c;
        int n = c.size();

        int maxDistance = 0;  // 원점으로부터의 최대 거리
        bool isInfinite = true;

        // 명령을 최대 4회 반복하여 주기 확인
        for (int count = 0; count < 4; ++count) {
            // 한 번의 명령어 전체 실행
            for (int i = 0; i < n; ++i) {
                if (c[i] == 'S') {
                    r.x += dx[r.dir];
                    r.y += dy[r.dir];
                }
                else if (c[i] == 'L') {
                    r.dir = (r.dir + 3) % 4;  // 왼쪽 회전
                }
                else if (c[i] == 'R') {
                    r.dir = (r.dir + 1) % 4;  // 오른쪽 회전
                }

                // 현재 위치에서 원점까지의 거리 계산
                int distance = r.x * r.x + r.y * r.y;
                maxDistance = max(maxDistance, distance);
            }

            // 명령을 모두 실행한 후 초기 위치와 방향으로 돌아왔는지 확인
            if (r.x == 0 && r.y == 0 && r.dir == 1) {
                isInfinite = false;  // 원래 위치로 돌아오면 무한히 멀어지지 않음
                break;
            }
        }

        // 출력
        if (isInfinite) {
            cout << "oo" << endl;
        }
        else {
            cout << (maxDistance) << endl;
        }
    }

    return 0;
}
