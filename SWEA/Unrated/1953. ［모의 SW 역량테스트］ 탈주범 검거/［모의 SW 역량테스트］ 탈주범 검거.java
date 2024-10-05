import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {

    private static class Pos {
        int x;
        int y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;

        }
    }

    private static final int[] dx = {-1, 0, 1, 0};
    private static final int[] dy = {0, 1, 0, -1};

    // 터널 종류
    private static final int[][] tunnel = {
            {0, 0, 0, 0},
            {1, 1, 1, 1},
            {1, 0, 1, 0},
            {0, 1, 0, 1},
            {1, 1, 0, 0},
            {0, 1, 1, 0},
            {0, 0, 1, 1},
            {1, 0, 0, 1}
    };

    static int[][] map;
    private static boolean[][] visited;

    static int N, M, R, C, L;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {
            sb = new StringBuilder();
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            R = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());
            L = Integer.parseInt(st.nextToken());

            map = new int[N][M];
            visited = new boolean[N][M];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < M; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            sb.append("#").append(t).append(" ").append(bfs(R, C));
            System.out.println(sb);
        }

    }

    private static int bfs(int sx, int sy) {
        int answer = 1;
        int hour = 0;

        ArrayDeque<Pos> queue = new ArrayDeque<>();
        queue.addLast(new Pos(sx, sy));

        visited[sx][sy] = true;

        while (!queue.isEmpty()) {
            if (hour == L - 1) {
                break;
            }

            int size = queue.size();

            while (size-- > 0) {
                Pos cur = queue.pollFirst();

                int[] d = tunnel[map[cur.x][cur.y]];

                for (int i = 0; i < d.length; i++) {
                    if (d[i] == 0) {
                        continue;
                    }

                    int nx = cur.x + dx[i];
                    int ny = cur.y + dy[i];

                    if (nx < 0 || ny < 0 || nx >= N || ny >= M) {
                        continue;
                    }

                    if (map[nx][ny] == 0) {
                        continue;
                    }

                    if (visited[nx][ny]) {
                        continue;
                    }

                    if (tunnel[map[nx][ny]][(i + 2) % 4] == 1) {
                        visited[nx][ny] = true;
                        queue.addLast(new Pos(nx, ny));
                        answer++;
                    }

                }

            }
            hour++;
        }
        return answer;
    }

}
