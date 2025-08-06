import java.util.*;

class Solution {
    public String solution(String s) {
        // 전체 문자열을 소문자로 변경
        s = s.toLowerCase();
        boolean check = true;
        StringBuilder sb = new StringBuilder();
        
        for (char c: s.toCharArray()) {
            // 문자가 공백이라면 -> 다음 글자가 단어의 첫글자
            if(c == ' ') {
                check = true;
            } else if(check) {
                // 대문자로 변경하고 첫 단어 check false
                c = Character.toUpperCase(c);
                check = false;
            }
            sb.append(c);
        }
        
        return sb.toString();
        
    }
}