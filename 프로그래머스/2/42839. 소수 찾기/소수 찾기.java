import java.util.*;

class Solution {
    static List<Integer> result;
    static boolean[] visited;
    
    public int solution(String numbers) {
        int answer = 0;
        
        visited = new boolean[7];
        result = new ArrayList<>();
        
        for(int i = 0; i < numbers.length(); i++) {
            permutation(numbers, "", i + 1);
        }
        
        for(int r : result) {
            if(isPrime(r)) {
                answer++;
            }
        }
        
        
        return answer;
    }
    
    static void permutation(String numbers, String cur, int depth) {
        if(cur.length() == depth) {
            int num = Integer.parseInt(new String(cur));
            if(!result.contains(num)) {
                result.add(num);
            }
            
            return;
        }
        
        for(int i = 0; i < numbers.length(); i++) {
            if(visited[i] == true) {
                continue;
            }
            
            visited[i] = true;
            permutation(numbers, cur + numbers.charAt(i), depth);
            visited[i] = false;
        }
    }
    
    static boolean isPrime(int x) {
        if (x < 2) {
            return false;
        }
        
        for(int i = 2; i <= (int) Math.sqrt(x); i++) {
            if(x % i == 0) {
                return false;
            }
        }
        
        return true;
    }
    
}