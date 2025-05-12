import java.io.*;
import java.util.*;

public class Main {

    static int n, m;
    static int[] arr;
    static int[] comb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        comb = new int[m];
        for (int i = 0; i < n; i++) {
            arr[i] = i + 1;
        }
        combination(0, 0);
    }

    static void combination(int depth, int start) {
        if (depth == m) {
            StringBuilder sb = new StringBuilder();

            for (int i = 0; i < m; i++) {
                sb.append(comb[i] + " ");
            }
            System.out.println(sb);
            return;
        }

        for (int i = start; i < n; i++) {
            comb[depth] = arr[i];
            combination(depth + 1, i + 1);
        }
    }

}
