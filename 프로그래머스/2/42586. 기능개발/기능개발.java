import java.util.*;

class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Deque<Integer> dq = new ArrayDeque<>();
        
        for(int i = 0; i < progresses.length; i++) {
            if((100 - progresses[i]) % speeds[i] == 0) {
                dq.addLast((100 - progresses[i]) / speeds[i]);
            } else {
                dq.addLast((100 - progresses[i]) / speeds[i] + 1);
            }
        }
        
        int curWorks = dq.removeFirst();
        int count = 1;
        
        while(!dq.isEmpty()) {
            if(curWorks >= dq.peekFirst()) {
                count++;
                dq.removeFirst();
            } else {
                answer.add(count);
                count = 1;
                curWorks = dq.removeFirst();
            }
        }
        
        answer.add(count);
        
        return answer;
    }
}