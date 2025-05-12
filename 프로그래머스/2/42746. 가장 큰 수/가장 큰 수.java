import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        String[] arr = new String[numbers.length];
        
        int index = 0;
        for(int n : numbers) {
            arr[index] = String.valueOf(n);
            index++;
        }
        
        Arrays.sort(arr, (s1, s2) -> (s2 + s1).compareTo(s1 + s2));
        
        if(arr[0].equals("0")) {
            return "0";
        }
        
        StringBuilder sb = new StringBuilder();
        
        for(String s : arr) {
            sb.append(s);
        }
        
        return sb.toString();
    }
}