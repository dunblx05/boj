import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    static int N, Q, C, sx, sy, ex, ey;
    // 상 우 하 좌
    static int direction;
    static char[] command;
    static char[][] map;

    static final int[] dx = {-1, 0, 1, 0};
    static final int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = null;

        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());
            map = new char[N][N];
            sb.append("#").append(tc).append(" ");

            for (int i = 0; i < N; i++) {
                String line = br.readLine();
                for (int j = 0; j < N; j++) {
                    map[i][j] = Character.toUpperCase(line.charAt(j));

                    if (map[i][j] == 'X') {
                        sx = i;
                        sy = j;
                        direction = 0;
                    }

                    if (map[i][j] == 'Y') {
                        ex = i;
                        ey = j;
                    }

                }
            }

            Q = Integer.parseInt(br.readLine());

            for (int i = 0; i < Q; i++) {
                int res;
                String[] commandLine = br.readLine().split(" ");
                C = Integer.parseInt(commandLine[0]);
                command = commandLine[1].toCharArray();

                int originalX = sx;
                int originalY = sy;

                for (char c : command) {
                    switch (c) {
                        case 'A':
                            move();
                            break;

                        case 'L':
                            // 0 -> 3 -> 2 -> 1
                            direction = (direction + 3) % 4;
                            break;

                        case 'R':
                            // 0 -> 1 -> 2 -> 3
                            direction = (direction + 1) % 4;
                            break;
                    }
                }

                if (sx == ex && sy == ey) {
                    res = 1;
                } else {
                    res = 0;
                }

                sb.append(res).append(" ");

                sx = originalX;
                sy = originalY;
                direction = 0;

            }
            sb.append("\n");

        }

        System.out.println(sb);
        
    }

    private static void move() {
        int nx = sx + dx[direction];
        int ny = sy + dy[direction];

        if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
            if (map[nx][ny] != 'T') {
                sx = nx;
                sy = ny;
            }
        }
    }
}
