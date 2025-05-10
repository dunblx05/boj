import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        Deque<Integer> q = new ArrayDeque<>();
        q.addLast(0);
        
        for(int i = 0; i < numbers.length; i++) {
            int size = q.size();
            for(int j = 0; j < size; j++) {
                int sum = q.removeFirst();
                q.addLast(sum + numbers[i]);
                q.addLast(sum - numbers[i]);
            }
        }
        
        while(!q.isEmpty()) {
            if(q.removeFirst() == target) {
                answer++;
            }
        }
        return answer;
    }
}