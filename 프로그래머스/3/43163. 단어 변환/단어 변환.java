import java.util.*;

class Solution {
    static boolean[] visited;
    static int answer = 0;
    
    public int solution(String begin, String target, String[] words) {
        visited = new boolean[words.length];
        dfs(begin, target, words, 0);
        
        return answer;
    }
    
    private static void dfs(String begin, String target, String[] words, int cnt) {
        // 종료조건
        if(begin.equals(target)) {
            answer = cnt;
            return;
        }
        
        for(int i = 0; i < words.length; i++) {
            if(visited[i]) {
                continue;
            }
            
            int diffWords = 0;
            // 단어에서 몇개의 스펠링이 다른지 확인
            for(int j = 0; j < begin.length(); j++) {
                if(begin.charAt(j) == words[i].charAt(j)) {
                    diffWords++;
                }
            }
            
            // 한글자빼고 다같다면
            // dfs
            if(diffWords == begin.length() - 1) {
                visited[i] = true;
                dfs(words[i], target, words, cnt + 1);
                visited[i] = false;
            }
            
        }
    }
}