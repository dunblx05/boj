import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = fibo(n);
        
        return answer;
    }
    
    private static int fibo(int n) {
        List<Integer> dp = new ArrayList<>();
        dp.add(0);
        dp.add(1);
        
        for(int i = 2; i < n + 1; i++) {
            int next = (dp.get(i - 1) + dp.get(i - 2)) % 1234567;
            dp.add(next);
        }
        
        return dp.get(n) % 1234567;
        
    }
}