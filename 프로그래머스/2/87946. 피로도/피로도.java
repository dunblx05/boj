import java.util.*;

class Solution {
    
    private static List<int[][]> result;
    private static boolean[] visited;
    private static int[][] cur;
    
    public int solution(int k, int[][] dungeons) {
        int answer = -1;
        visited = new boolean[dungeons.length];
        result = new ArrayList<>();
        // 현재 순열 저장 배열
        cur = new int[dungeons.length][2];
        
        permutation(dungeons, 0);
        
        for(int[][] perm : result) {
            int tired = k;
            int count = 0;
            
            for(int[] p : perm) {
                if(tired >= p[0]) {
                    tired -= p[1];
                    count++;
                }
            }
            if(count >= answer) {
                answer = count;
            }
            
        }
        return answer;
    }
    
    private static void permutation(int dungeons[][], int length) {
        if (length == dungeons.length) {
            // 완성된 순열 복사해서 저장
            int[][] copy = new int[dungeons.length][2];
            for (int i = 0; i < dungeons.length; i++) {
                copy[i][0] = cur[i][0];
                copy[i][1] = cur[i][1];
            }
            result.add(copy);
            return;
        }
        
        for(int i = 0; i < dungeons.length; i++) {
            if(visited[i] == true) {
                continue;
            }
            visited[i] = true;
            cur[length] = dungeons[i];
            permutation(dungeons, length + 1);
            visited[i] = false;
        }
    }
}