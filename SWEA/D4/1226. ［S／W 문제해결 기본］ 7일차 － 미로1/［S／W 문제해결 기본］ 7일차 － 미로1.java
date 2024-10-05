import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Solution {

    private static int[][] maze;
    private static boolean[][] visited;

    private static final int[] dx = {-1, 0, 1, 0};
    private static final int[] dy = {0, 1, 0, -1};

    private static class Pair {
        int x;
        int y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for (int t = 1; t < 11; t++) {
            int tc = Integer.parseInt(br.readLine());

            maze = new int[16][16];
            visited = new boolean[16][16];

            int sx = 1;
            int sy = 1;

            // 입력 부분
            for (int i = 0; i < 16; i++) {
                String s = br.readLine();

                for (int j = 0; j < 16; j++) {
                    maze[i][j] = s.charAt(j) - '0';
                }
            }

            int res = bfs(sx, sy);

            System.out.println("#" + t + " " + res);

        }

    }

    private static int bfs(int sx, int sy) {
        ArrayDeque<Pair> queue = new ArrayDeque<>();
        queue.addLast(new Pair(sx, sy));

        visited[sx][sy] = true;

        while (!queue.isEmpty()) {
            Pair cur = queue.pollFirst();

            int x = cur.x;
            int y = cur.y;

            if (maze[x][y] == 3) {
                return 1;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || ny < 0 || nx >= 16 || ny >= 16) {
                    continue;
                }

                if (maze[nx][ny] != 1 && !visited[nx][ny]) {
                    queue.addLast(new Pair(nx, ny));
                    visited[nx][ny] = true;

                }
            }
        }

        return 0;
    }
}