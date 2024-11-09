#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int N, X, M;  // N: 배열의 크기, X: 각 원소의 최대값, M: 조건의 수
int sum, maX; // sum: 현재 배열의 합, maX: 가능한 최대 배열 합

// 조건을 저장할 구조체 정의
struct pos {
    int l; // 시작 인덱스
    int r; // 끝 인덱스
    int s; // 해당 범위의 목표 합
};

vector<pos> loog;  // 조건들을 저장하는 벡터
int arr[1001];     // 배열의 값들
int ans[1001];     // 최종 답으로 사용할 배열

// DFS를 이용한 모든 경우 탐색
void dfs(int cnt) {
    // N개의 값을 모두 할당했을 때
    if (cnt == N + 1) {
        // 현재 배열의 합이 maX보다 크면 갱신 시도
        if (maX < sum) {
            // 모든 조건을 검사하여 만족하는지 확인
            for (int i = 0; i < loog.size(); i++) {
                int subsum = 0;
                for (int j = loog[i].l; j <= loog[i].r; j++) {
                    subsum += arr[j];
                }
                // 조건 중 하나라도 만족하지 않으면 종료
                if (subsum != loog[i].s) return;
            }

            // 조건을 모두 만족하면, 최대 합과 배열 갱신
            maX = sum;
            for (int i = 1; i <= N; i++)
                ans[i] = arr[i];
        }
        return;
    }

    // 각 원소를 0에서 X까지 할당하며 DFS 진행
    for (int i = 0; i <= X; i++) {
        arr[cnt] = i;   // 현재 인덱스의 값을 i로 설정
        sum += i;       // 합에 추가
        dfs(cnt + 1);   // 다음 인덱스로 이동
        sum -= i;       // 백트래킹을 위해 합에서 제거
        arr[cnt] = 0;   // 백트래킹을 위해 값 초기화
    }
}

int main() {
    int T; // 테스트 케이스의 수
    cin >> T;

    for (int testcase = 1; testcase <= T; testcase++) {
        memset(ans, 0, sizeof(ans)); // 이전 테스트의 답 초기화
        loog.clear();                // 조건 리스트 초기화
        maX = sum = 0;
        maX = -1; // 초기 maX를 -1로 설정하여 실패 여부 확인

        cin >> N >> X >> M; // 배열 크기, 원소 최대값, 조건 수 입력

        // 조건 입력받아 loog 벡터에 추가
        int l, r, s;
        for (int i = 0; i < M; i++) {
            cin >> l >> r >> s;
            loog.push_back({ l, r, s });
        }

        dfs(1); // DFS 탐색 시작

        // 조건을 만족하는 배열이 없는 경우
        if (maX == -1) {
            cout << "#" << testcase << " -1\n";
            continue;
        }

        // 조건을 만족하는 배열이 있는 경우 출력
        cout << "#" << testcase;
        for (int i = 1; i <= N; i++) {
            cout << " " << ans[i];
        }
        cout << "\n";
    }

    return 0;
}
