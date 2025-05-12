import java.io.*;
import java.util.*;

public class Main {

    static int n, m;
    static boolean[] visited;
    static int[] arr;
    static int[] per;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        // 순열 배열
        per = new int[m];

        for (int i = 0; i < n; i++) {
            arr[i] = i + 1;
        }

        visited = new boolean[n];

        permutation(0);

    }

    static void permutation(int depth) {
        // m개 선택했다면 종료
        if (depth == m) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < m; i++) {
                sb.append(per[i] + " ");
            }
            System.out.println(sb);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }
            visited[i] = true;
            per[depth] = arr[i];
            permutation(depth + 1);
            visited[i] = false;
        }
    }
}
