import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		StringBuilder sb = new StringBuilder();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int t = Integer.parseInt(br.readLine());

		for (int i = 0; i < t; i++) {

			int n = Integer.parseInt(br.readLine());
			int max = Integer.MIN_VALUE;
			int min = Integer.MAX_VALUE;

			st = new StringTokenizer(br.readLine(), " ");

			for (int j = 0; j < n; j++) {

				int num = Integer.parseInt(st.nextToken());

				if (num < min) {
					min = num;
				}
				if (num > max) {
					max = num;
				}

			}
			sb.append(min + " " + max + "\n");
		}

		System.out.println(sb.toString());
	}

}