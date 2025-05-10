import java.util.*;

class Solution {
    
    static boolean[] visited;
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        
        for(int i = 0; i < n; i++) {
            if(visited[i] == false) {
                bfs(i, n, computers);
                answer++;
            }
        }
        return answer;
    }
    
    public static void bfs(int start, int n, int[][] computers) {
        Deque<Integer> q = new ArrayDeque<>();
        visited[start] = true;
        q.addLast(start);
        
        while(!q.isEmpty()) {
            int curNode = q.removeFirst();
            
            for(int i = 0; i < n; i++) {
                if(visited[i] == true) {
                    continue;
                }
                if(computers[curNode][i] == 0) {
                    continue;
                }
                
                visited[i] = true;
                q.addLast(i);
                
            }
            
        }
        
    }
    
}