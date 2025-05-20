import java.util.*;

class Solution {
    static int MAX = Integer.MIN_VALUE;
    static int MIN = Integer.MAX_VALUE;
    
    public StringBuilder solution(String s) {
        List<Integer> l = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(s);
        
        while(st.hasMoreTokens()) {
            l.add(Integer.parseInt(st.nextToken()));
        }
        
        for(int i : l) {
            MAX = Math.max(i, MAX);
            MIN = Math.min(i, MIN);
        }
        
        sb.append(MIN + " " + MAX);
        return sb;
    }
}