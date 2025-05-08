import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        HashMap<String, Integer> map = new HashMap<>();
        
        for(String[] cloth : clothes) {
            String clothName = cloth[0];
            String clothType = cloth[1];
            
            map.put(clothType, map.getOrDefault(clothType, 0) + 1);
        }
        
        for(int count : map.values()) {
            answer *= (count + 1);
        }
        
        
        return answer - 1;
    }
}