import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for (int i = 0; i < t; i++) {

			int n = sc.nextInt();
			int max = Integer.MIN_VALUE;
			int min = Integer.MAX_VALUE;

			for (int j = 0; j < n; j++) {

				int num = sc.nextInt();
				
				if (num < min) {
					min = num;
				}
				if (num > max) {
					max = num;
				}

			}
			System.out.printf(min + " " + max + "\n");

		}

		sc.close();
	}

}