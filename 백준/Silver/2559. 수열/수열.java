import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int answer = 0;

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] temperature = new int[n];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            temperature[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < k; i++) {
            answer = answer + temperature[i];
        }

        int temp = answer;

        for (int i = k; i < n; i++) {
            temp = temp - temperature[i - k] + temperature[i];
            answer = Math.max(answer, temp);
        }

        System.out.println(answer);

    }
}