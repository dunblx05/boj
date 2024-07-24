import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		
		StringBuilder sb = new StringBuilder();
		String[] binary = {"000", "001", "010", "011", "100", "101", "110", "111"};
		
		for(int i = 0; i < s.length(); i++) {
			
			// String을 int로 변환
			int a = s.charAt(i) - '0';
			sb.append(binary[a]);
		}
		
		if (s.equals("0")) {
			System.out.println(s);
		}
		else {
			
			while (sb.charAt(0) == '0') {
				sb = new StringBuilder(sb.substring(1));
			}
			System.out.println(sb);
			
		}
		
	}

}
