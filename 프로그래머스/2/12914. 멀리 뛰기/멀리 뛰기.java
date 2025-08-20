import java.util.*;

class Solution {
    public long solution(int n) {
        // 기저 조건
        if (n == 1) return 1;
        if (n == 2) return 2;
        
        // DP 배열 초기화
        long[] dp = new long[n + 1];
        dp[1] = 1;  // 1칸에 도달하는 방법: (1칸)
        dp[2] = 2;  // 2칸에 도달하는 방법: (1칸,1칸), (2칸)
        
        // 동적 프로그래밍으로 해결
        for (int i = 3; i <= n; i++) {
            // i칸에 도달하는 방법 = (i-1)칸에서 1칸 뛰기 + (i-2)칸에서 2칸 뛰기
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
        }
        
        return dp[n];
    }
}