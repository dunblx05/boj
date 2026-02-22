import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static int r, c, d;

    // d = 0, 1, 2, 3
    // 북 -> 동 -> 남 -> 서 -> 북
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    static int[][] room = new int[51][51];
    static boolean[][] clean = new boolean[51][51];

    static int count = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < M; j++) {
                room[i][j] = Integer.parseInt(st.nextToken());
            }

        }

        simulation();

        System.out.println(count);

    }

    private static void simulation() {

        while (true) {

            boolean isMoved = false;

            if (!clean[r][c]) {
                clean[r][c] = true;
                count++;
            }

            for (int i = 0; i < 4; i++) {
                d = (d + 3) % 4;

                int nx = r + dx[d];
                int ny = c + dy[d];

                if (nx < 0 || ny < 0 || nx >= N || ny >= M) {
                    continue;
                }

                if (!clean[nx][ny] && room[nx][ny] == 0) {
                    r = nx;
                    c = ny;

                    isMoved = true;

                    break;
                }
            }

            if (!isMoved) {

                if (room[r - dx[d]][c - dy[d]] == 1) {
                    break;
                } else {
                    r = r - dx[d];
                    c = c - dy[d];
                }

            }

        }

    }

}
