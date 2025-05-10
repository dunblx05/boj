import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int maxW = 0;
        int maxH = 0;
        
        for(int[] size : sizes) {
            int w = size[0];
            int h = size[1];
            
            if (w > h) {
                size[0] = h;
                size[1] = w;
            }
        }
        
        for(int [] size: sizes) {
            if(maxW < size[0]) {
                maxW = size[0];
            }
            
            if(maxH < size[1]) {
                maxH = size[1];
            }
        }
        
        answer = maxW * maxH;
        
        return answer;
    }
}