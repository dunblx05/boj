import java.util.*;

class Solution {
    public List<Integer> solution(String s) {
        int count = 0;
        int totalZero = 0;
        
        List<Integer> answer = new ArrayList<>();
        
        while(s.length() > 1) {
            int remainLength = 0;
            int zeroCount = 0;
            
            for(char c : s.toCharArray()) {
                if(c == '0') {
                    zeroCount++;
                }
            }
            
            totalZero += zeroCount;
            remainLength = s.length() - zeroCount;
            s = Integer.toBinaryString(remainLength);
            count++;
        }
        answer.add(count);
        answer.add(totalZero);
        return answer;
    }
}