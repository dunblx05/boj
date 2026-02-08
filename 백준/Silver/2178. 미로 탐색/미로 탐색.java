import java.util.*;
import java.io.*;

public class Main {

    static int N, M;
    static int[][] maze = new int[101][101];

    // 상, 우, 하, 좌
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    static class Pos {
        int x;
        int y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            String s = br.readLine();

            for (int j = 0; j < M; j++) {
                maze[i][j] = s.charAt(j) - '0';
            }
        }

        bfs();

        System.out.print(maze[N - 1][M - 1]);

    }

    private static void bfs() {
        Deque<Pos> q = new ArrayDeque<>();

        q.addLast(new Pos(0, 0));

        while (!q.isEmpty()) {
            Pos curPos = q.removeFirst();

            for (int i = 0; i < 4; i++) {
                int nx = curPos.x + dx[i];
                int ny = curPos.y + dy[i];

                if (nx < 0 || ny < 0 || nx >= N || ny >= M) {
                    continue;
                }

                if (maze[nx][ny] == 0) {
                    continue;
                }

                if (maze[nx][ny] == 1) {
                    maze[nx][ny] = maze[curPos.x][curPos.y] + 1;
                    q.addLast(new Pos(nx, ny));
                }

            }

        }
    }

}
