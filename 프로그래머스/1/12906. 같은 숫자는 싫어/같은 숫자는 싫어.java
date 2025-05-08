import java.util.*;

public class Solution {
    public Stack<Integer> solution(int []arr) {
        Stack<Integer> stack = new Stack<>();
        
        for(int n : arr) {
            if(stack.isEmpty()) {
                stack.push(n);
            }
            if(n != stack.peek() && !stack.isEmpty()) {
                stack.push(n);                
            }
        }
        
        return stack;
    }
}