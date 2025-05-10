import java.util.*;

class Solution {
    public List<Integer> solution(int[] prices) {
        List<Integer> answer = new ArrayList<>();
        
        Deque<Integer> q = new ArrayDeque<>();
        
        for(int price : prices) {
            q.addLast(price);
        }
        
        while(!q.isEmpty()) {
            int curPrice = q.removeFirst();
            int time = 0;
            
            for(int price : q) {
                if(curPrice <= price) {
                    time++;
                } else {
                    time++;
                    break;
                }
            }
            answer.add(time);
        }
        
        return answer;
    }
}