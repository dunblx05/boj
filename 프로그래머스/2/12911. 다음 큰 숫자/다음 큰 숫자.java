import java.util.*;

class Solution {
    public int solution(int n) {
        
        String nBinary = Integer.toBinaryString(n);
        int count = 0;
        int answer = 0;
        
        for(char c : nBinary.toCharArray()) {
            if(c == '1') {
                count++;
            }
        }
        
        for(int i = n + 1; i < 1000000; i++) {
            String iBinary = Integer.toBinaryString(i);
            int countOne = 0;
            
            for(char c : iBinary.toCharArray()) {
                if(c == '1') {
                    countOne++;
                }
            }
            
            if(countOne == count) {
                answer = i;
                break;
            }
            
        }
        
        return answer;
    }
}