import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        HashMap<String, Integer> map = new HashMap<>();
        
        for(String p : phone_book) {
            map.put(p, 1);
        }
        
        for(String p : phone_book) {
            StringBuilder sb = new StringBuilder();
            
            for(int i = 0; i < p.length() - 1; i++) {
                sb.append(p.charAt(i));
                
                if(map.containsKey(sb.toString())) {
                    return false;
                }
                
            }
        }
        
        return true;
    }
}