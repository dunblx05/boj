import java.util.*;
import java.io.*;

public class Main {

    static int N, M;
    static int[][] lab = new int[9][9];

    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    static int answer;

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
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < M; j++) {
                lab[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        buildWall(0);

        System.out.println(answer);
    }

    private static void buildWall(int count) {
        if (count == 3) {
            bfs();
            return;
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (lab[i][j] == 0) {
                    lab[i][j] = 1;
                    buildWall(count + 1);
                    lab[i][j] = 0;
                }
            }
        }

    }

    private static void bfs() {
        int[][] tempLab = new int[N][M];
        boolean[][] visited = new boolean[N][M];

        Deque<Pos> q = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                tempLab[i][j] = lab[i][j];

                if (tempLab[i][j] == 2) {
                    q.addLast(new Pos(i, j));
                    visited[i][j] = true;
                }

            }
        }

        while (!q.isEmpty()) {
            Pos curPos = q.removeFirst();

            for (int i = 0; i < 4; i++) {
                int nx = curPos.x + dx[i];
                int ny = curPos.y + dy[i];

                if (nx < 0 || ny < 0 || nx >= N || ny >= M) {
                    continue;
                }

                if (!visited[nx][ny] && tempLab[nx][ny] == 0) {
                    q.addLast(new Pos(nx, ny));
                    visited[nx][ny] = true;
                    tempLab[nx][ny] = 2;
                }

            }

        }

        int safeArea = countSafe(tempLab);

        answer = Math.max(safeArea, answer);

    }

    private static int countSafe(int[][] map) {

        int safeArea = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 0) {
                    safeArea += 1;
                }

            }
        }

        return safeArea;
    }
}
