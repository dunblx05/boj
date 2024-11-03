#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <stack>
#include <cstring>
using namespace std;

#define endl '\n'

typedef long long ll;

// 상하좌우 이동을 위한 방향 배열
int dx[] = {-1, 0, 1, 0}; // 상, 우, 하, 좌
int dy[] = {0, 1, 0, -1};

int answer; // 최소 블록 수
int T, N, W, H; // 테스트 케이스 수, 공 발사 횟수, 너비, 높이
int board[16][13]; // 원본 게임 보드
int tempBoard[16][13]; // 작업 중인 게임 보드
int visited[16][13]; // 방문한 블록 표시
int order[6]; // 발사 순서

// 블록의 정보를 저장하는 구조체
struct info {
    int x; // 블록의 x 좌표
    int y; // 블록의 y 좌표
    int power; // 블록의 파괴력
};

// 블록을 파괴하는 함수
void breakBlock(int sx, int sy, int sp) {
    memset(visited, 0, sizeof(visited)); // 방문 배열 초기화
    queue<info> q; // BFS를 위한 큐
    visited[sx][sy] = 1; // 시작 블록 방문 표시

    q.push({sx, sy, sp}); // 시작 블록을 큐에 추가
    tempBoard[sx][sy] = 0; // 블록 파괴

    while (!q.empty()) {
        info cur = q.front(); // 큐의 맨 앞 요소를 가져옴
        q.pop();

        int x = cur.x; // 현재 블록의 x 좌표
        int y = cur.y; // 현재 블록의 y 좌표
        int power = cur.power; // 현재 블록의 파괴력

        // 블록의 파괴력이 1 이상인 경우 주변 블록 파괴
        for (int i = 1; i < power; ++i) {
            for (int j = 0; j < 4; ++j) {
                int nx = x + dx[j] * i; // 새로운 x 좌표
                int ny = y + dy[j] * i; // 새로운 y 좌표

                // 경계 체크
                if (nx < 0 || ny < 0 || nx >= H || ny >= W) {
                    continue;
                }

                // 이미 방문한 블록이거나 파괴된 블록은 무시
                if (visited[nx][ny] == 1 || tempBoard[nx][ny] == 0) {
                    continue;
                }

                // 새로운 블록을 큐에 추가하고 방문 표시
                q.push({nx, ny, tempBoard[nx][ny]});
                visited[nx][ny] = 1;
                tempBoard[nx][ny] = 0; // 블록 파괴
            }
        }
    }
}

// 블록을 아래로 내리는 함수
void downBlock() {
    for (int j = 0; j < W; ++j) { // 각 열에 대해
        stack<int> s; // 블록을 저장할 스택

        // 현재 열의 모든 블록을 스택에 저장
        for (int i = 0; i < H; ++i) {
            if (tempBoard[i][j] != 0) {
                s.push(tempBoard[i][j]);
            }
        }

        // 스택에서 블록을 꺼내어 아래로 내림
        for (int i = H - 1; i >= 0; --i) {
            if (s.empty()) {
                tempBoard[i][j] = 0; // 빈 공간
            } else {
                tempBoard[i][j] = s.top(); // 블록을 아래로 내림
                s.pop();
            }
        }
    }
}

// 남아있는 블록 수를 세는 함수
int countBlock() {
    int cnt = 0;

    // 모든 블록을 탐색하여 남아있는 블록 수 카운트
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (tempBoard[i][j] != 0) {
                cnt++;
            }
        }
    }
    return cnt; // 남아있는 블록 수 반환
}

// 공을 발사하는 함수
void shoot() {
    // 작업 보드를 원본으로 초기화
    memcpy(tempBoard, board, sizeof(board));

    // N번의 공 발사
    for (int i = 0; i < N; ++i) {
        int x = -1; // 발사한 블록의 x 좌표
        int y = order[i]; // 발사할 열

        // 가장 위의 블록 찾기
        for (int j = 0; j < H; ++j) {
            if (tempBoard[j][y] > 0) {
                x = j;
                break;
            }
        }

        // 발사할 블록이 없으면 계속 진행
        if (x == -1) {
            continue;
        }

        // 블록 파괴 및 아래로 내리기
        breakBlock(x, y, tempBoard[x][y]);
        downBlock();
    }

    int res = countBlock(); // 남아있는 블록 수 카운트
    answer = min(answer, res); // 최소 블록 수 갱신
}

// 발사 순서를 선택하는 함수 (중복 조합)
void selectTop(int depth) {
    if (depth == N) { // N번의 발사가 완료되면
        shoot(); // 발사 시뮬레이션 수행
        return;
    }

    // 각 열에 대해 발사 순서 설정
    for (int i = 0; i < W; ++i) {
        order[depth] = i; // 현재 깊이에 해당하는 열을 선택
        selectTop(depth + 1); // 다음 깊이로 진행
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> T; // 테스트 케이스 수 입력

    for (int tc = 1; tc <= T; ++tc) {
        cin >> N >> W >> H; // 공 발사 횟수, 보드의 너비와 높이 입력

        answer = 181; // 초기 답변값 설정 (최대 블록 수보다 큰 값)

        // 보드 초기화
        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < W; ++j) {
                cin >> board[i][j];
            }
        }

        selectTop(0); // 가능한 모든 발사 조합 시도

        cout << "#" << tc << ' ' << answer << endl; // 결과 출력
    }
}
