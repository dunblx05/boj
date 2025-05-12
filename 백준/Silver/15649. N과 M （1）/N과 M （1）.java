import java.util.*;
import java.io.*;

public class Main {

    static int n, m;
    static List<List<Integer>> result;
    static List<Boolean> visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());  // ✅ 클래스 변수로 초기화
        m = Integer.parseInt(st.nextToken());

        List<Integer> arr = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();
        result = new ArrayList<>();
        visited = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            arr.add(i);
            visited.add(false);
        }

        permutation(arr, m, cur, visited);

        for (List<Integer> r : result) {
            for (int num : r) {
                System.out.print(num + " ");  // ✅ println → print 로 변경
            }
            System.out.println();
        }
    }

    static void permutation(List<Integer> arr, int r, List<Integer> cur, List<Boolean> visited) {
        if (cur.size() == r) {
            result.add(new ArrayList<>(cur)); // ✅ 깊은 복사로 저장
            return;
        }

        for (int i = 0; i < arr.size(); i++) {
            if (visited.get(i)) continue;

            visited.set(i, true);
            cur.add(arr.get(i));
            permutation(arr, r, cur, visited);
            cur.remove(cur.size() - 1);
            visited.set(i, false);
        }
    }
}
