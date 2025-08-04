import java.io.*;
import java.util.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int M, N;
    private static boolean[] isPrime;

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성하세요
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        StringBuilder sb = new StringBuilder();

        // M, N 입력
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        // 소수 판별 배열 초기화
        boolean[] isPrime = new boolean[N + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;

        // 체 알고리즘
        for (int i = 2; i * i <= N; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= N; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        for (int i = M; i <= N; i++) {
            if (isPrime[i]) {
                sb.append(i).append("\n");
            }
        }

        System.out.println(sb);

    }
}