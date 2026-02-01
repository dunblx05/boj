import java.util.*;
import java.io.*;

public class Main {

    static int M, N, H;
    static int[][][] tomatoes = new int[101][101][101];

    static int[] dx = {-1, 0, 1, 0, 0, 0};
    static int[] dy = {0, 1, 0, -1, 0, 0};
    static int[] dz = {0, 0, 0, 0, -1, 1};

    static class Pos {

        // 높이, 가로, 세로
        int z;
        int y;
        int x;


        public Pos(int z, int y, int x) {
            this.z = z;
            this.y = y;
            this.x = x;
        }
    }

    static Deque<Pos> q = new ArrayDeque<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < N; j++) {
                st = new StringTokenizer(br.readLine());

                for (int k = 0; k < M; k++) {
                    tomatoes[i][j][k] = Integer.parseInt(st.nextToken());

                    if (tomatoes[i][j][k] == 1) {
                        q.addLast(new Pos(i, j, k));
                    }
                }

            }
        }

        bfs();

        int max = 0;

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < M; k++) {
                    if (tomatoes[i][j][k] == 0) {
                        System.out.println(-1);
                        return;
                    }

                    max = Math.max(max, tomatoes[i][j][k]);
                }
            }
        }

        System.out.println(max - 1);

    }

    private static void bfs() {

        while (!q.isEmpty()) {
            Pos curPos = q.removeFirst();

            for (int i = 0; i < 6; i++) {
                int nx = curPos.x + dx[i];
                int ny = curPos.y + dy[i];
                int nz = curPos.z + dz[i];

                if (nx < 0 || ny < 0 || nz < 0 || nx >= M || ny >= N || nz >= H) {
                    continue;
                }

                if (tomatoes[nz][ny][nx] != 0) {
                    continue;
                }

                tomatoes[nz][ny][nx] = tomatoes[curPos.z][curPos.y][curPos.x] + 1;
                q.addLast(new Pos(nz, ny, nx));
            }
        }
    }
}
