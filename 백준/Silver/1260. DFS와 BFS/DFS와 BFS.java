import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;
import java.util.ArrayDeque;

public class Main {

    private static int N;
    private static int M;
    private static int V;

    private static List<Integer>[] graph;
    private static boolean[] visited;

    private static StringBuilder dfsResult = new StringBuilder();
    private static StringBuilder bfsResult = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a].add(b);
            graph[b].add(a);
        }

        for (int i = 1; i <= N; i++) {
            Collections.sort(graph[i]);
        }

        visited = new boolean[N + 1];
        dfs(V);
        System.out.println(dfsResult.toString().trim());

        visited = new boolean[N + 1];
        bfs(V);
        System.out.println(bfsResult.toString().trim());

    }

    private static void dfs(int v) {
        visited[v] = true;
        dfsResult.append(v).append(" ");

        for (int next : graph[v]) {
            if (!visited[next]) {
                dfs(next);
            }
        }
    }

    private static void bfs(int v) {
        ArrayDeque<Integer> q = new ArrayDeque<>();

        q.addLast(v);
        visited[v] = true;

        while (!q.isEmpty()) {
            int cur = q.removeFirst();
            bfsResult.append(cur).append(" ");

            for (int next : graph[cur]) {
                if (!visited[next]) {
                    q.addLast(next);
                    visited[next] = true;
                }
            }
        }
    }

}