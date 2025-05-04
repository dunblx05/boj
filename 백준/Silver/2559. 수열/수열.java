import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] temperature = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            temperature[i] = Integer.parseInt(st.nextToken());
        }

        // 첫 k일의 합으로 초기화
        int sum = 0;
        for (int i = 0; i < k; i++) {
            sum += temperature[i];
        }

        int max = sum;

        // 슬라이딩 윈도우로 최대 합 계산
        for (int i = k; i < n; i++) {
            sum += temperature[i] - temperature[i - k];
            max = Math.max(max, sum);
        }

        System.out.println(max);
    }
}
