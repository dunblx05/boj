import java.util.*;
import java.io.*;

public class Main {

    static int T;
    static int[][] board = new int[301][301];

    // 나이트의 이동방향
    static int[] dx = {1, 2, 2, 1, -1, -2, -2, -1};
    static int[] dy = {2, 1, -1, -2, -2, -1, 1, 2};

    // 위치
    static class Pos {
        int x;
        int y;
        int move;

        public Pos(int x, int y, int move) {
            this.x = x;
            this.y = y;
            this.move = move;
        }
    }

    // 방문 배열
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // 테스트 횟수
        T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            // 체스판 크기
            int l = Integer.parseInt(br.readLine());

            visited = new boolean[l][l];

            // 나이트 시작 위치
            StringTokenizer st = new StringTokenizer(br.readLine());
            int sX = Integer.parseInt(st.nextToken());
            int sY = Integer.parseInt(st.nextToken());

            // 나이트 도착 위치
            st = new StringTokenizer(br.readLine());
            int eX = Integer.parseInt(st.nextToken());
            int eY = Integer.parseInt(st.nextToken());

            sb.append(bfs(sX, sY, eX, eY, l)).append('\n');

        }

        System.out.println(sb);
    }

    public static int bfs(int sX, int sY, int eX, int eY, int size) {

        Deque<Pos> q = new ArrayDeque<>();
        q.addLast(new Pos(sX, sY, 0));
        visited[sX][sY] = true;

        while (!q.isEmpty()) {
            Pos curPos = q.removeFirst();

            if (curPos.x == eX && curPos.y == eY) {
                return curPos.move;
            }

            for (int i = 0; i < 8; i++) {
                int nx = curPos.x + dx[i];
                int ny = curPos.y + dy[i];

                // 범위 밖으로 나간 경우
                if (nx < 0 || ny < 0 || nx >= size || ny >= size) {
                    continue;
                }

                // 방문한 경우
                if (visited[nx][ny]) {
                    continue;
                }

                visited[nx][ny] = true;
                q.addLast(new Pos(nx, ny, curPos.move + 1));

            }

        }
        return 0;
    }
}
