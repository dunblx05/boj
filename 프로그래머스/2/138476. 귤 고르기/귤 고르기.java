import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int t : tangerine) {
            map.put(t, map.getOrDefault(t, 0) + 1);
        }
        
        List<Integer> keys = new ArrayList<>(map.keySet());
        keys.sort(((o1, o2) -> map.get(o2) - map.get(o1)));
        
        int i = 0;
        while (k > 0) {
            k -= map.get(keys.get(i));
            answer++;
            i++;
        }
        
        return answer;
    }
}