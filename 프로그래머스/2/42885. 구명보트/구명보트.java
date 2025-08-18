import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int minIndex = 0;
        int maxIndex = people.length - 1;
        
        Arrays.sort(people);
        
        for(int i = maxIndex; minIndex <= i; i--) {
            if(people[minIndex] + people[i] <= limit) {
                minIndex++;
            }
            answer++;
        }
        
        
        return answer;
    }
}