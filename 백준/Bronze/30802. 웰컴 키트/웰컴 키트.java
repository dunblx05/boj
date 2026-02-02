import java.io.*;
import java.util.*;

public class Main {

    static int N, T, P;
    static List<Integer> sizeList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < 6; i++) {
            sizeList.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());

        T = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());

        int shirts = 0;

        for (int s : sizeList) {
            shirts += s / T;

            if(s % T > 0) {
                shirts += 1;
            }

        }

        System.out.println(shirts);
        System.out.println(N / P + " " + N % P);

    }
}