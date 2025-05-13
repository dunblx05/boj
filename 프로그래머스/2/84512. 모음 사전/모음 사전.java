import java.util.*;

class Solution {
    private static String words = "AEIOU";
    private static List<String> wordList;
    
    public int solution(String word) {
        int answer = 0;
        wordList = new ArrayList<>();
        
        allWords(0, "");
        
        answer = wordList.indexOf(word) + 1;
        
        return answer;
    }
    
    private static void allWords(int depth, String cur) {
        if(depth == 5) {
            return;
        }
        for(int i = 0; i < words.length(); i++) {
            wordList.add(cur + words.charAt(i));
            allWords(depth + 1, cur + words.charAt(i));
        }
    }
}