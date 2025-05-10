import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Deque<Integer> q = new ArrayDeque<>();
        int sum = 0;
        int time = 0;
        
        for(int truck : truck_weights) {
            while(true) {
                if(q.isEmpty()) {
                    q.addLast(truck);
                    sum += truck;
                    time++;
                    break;
                } else if(q.size() == bridge_length) {
                    sum -= q.removeFirst();
                } else {
                    if(sum + truck <= weight) {
                        q.addLast(truck);
                        sum += truck;
                        time++;
                        break;
                    } else {
                        q.addLast(0);
                        time++;
                    }
                }
            }
        }
        
        return time + bridge_length;
    }
}