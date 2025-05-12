import java.io.*;
import java.util.*;

public class Main {

    static int n, m;
    static int[] arr;
    static int[] cur;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        cur = new int[m];  // ✅ 여기서 제대로 m으로 크기 맞춰 초기화

        for (int i = 0; i < n; i++) {
            arr[i] = i + 1;
        }

        combination(0, 0);
    }

    static void combination(int depth, int start) {
        if (depth == m) {
            for (int i = 0; i < m; i++) {
                System.out.print(cur[i] + " ");
            }
            System.out.println();
            return;
        }

        for (int i = start; i < n; i++) {
            cur[depth] = arr[i];
            combination(depth + 1, i + 1);
        }
    }
}
