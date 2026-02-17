import java.util.*;
import java.io.*;

public class Main {

    static int N, M;
    static int[][] northPole = new int[301][301];
    static int[][] meltCount = new int[301][301];
    static boolean[][] visited = new boolean[301][301];

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
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < M; j++) {
                northPole[i][j] = Integer.parseInt(st.nextToken());
            }

        }

        int year = 0;

        while (true) {
            int ices = 0;
            visited = new boolean[N][M];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (northPole[i][j] > 0 && !visited[i][j]) {
                        countIce(i, j);
                        ices++;
                    }
                }
            }

            if (ices >= 2) {
                System.out.println(year);
                break;
            } else if (ices == 0) {
                System.out.println(0);
                break;
            } else {
                melt();

                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < M; j++) {
                        northPole[i][j] = Math.max(0, northPole[i][j] - meltCount[i][j]);
                    }
                }

                year++;
            }

        }

    }

    private static void melt() {

        meltCount = new int[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {

                if (northPole[i][j] > 0) {

                    for (int k = 0; k < 4; k++) {
                        int nx = i + dx[k];
                        int ny = j + dy[k];

                        if (nx < 0 || ny < 0 || nx >= N || ny >= M) {
                            continue;
                        }

                        if (northPole[nx][ny] == 0) {
                            meltCount[i][j] += 1;
                        }


                    }

                }

            }
        }
    }

    private static void countIce(int sx, int sy) {

        Deque<Pos> q = new ArrayDeque<>();

        q.addLast(new Pos(sx, sy));
        visited[sx][sy] = true;

        while (!q.isEmpty()) {
            Pos curPos = q.removeFirst();

            for (int i = 0; i < 4; i++) {
                int nx = curPos.x + dx[i];
                int ny = curPos.y + dy[i];

                if (nx < 0 || ny < 0 || nx >= N || ny >= M) {
                    continue;
                }

                if (visited[nx][ny]) {
                    continue;
                }

                if (northPole[nx][ny] == 0) {
                    continue;
                }

                q.addLast(new Pos(nx, ny));
                visited[nx][ny] = true;

            }

        }


    }
}
