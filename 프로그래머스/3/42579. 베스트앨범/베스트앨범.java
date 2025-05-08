import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        
        // 장르별 총 재생 횟수
        HashMap<String, Integer> playedCount = new HashMap<>();
        // 장르에 속하는 음악과 음악별 총 재생 횟수 
        HashMap<String, HashMap<Integer, Integer>> musicInfo = new HashMap<>();
        
        for(int i = 0; i < plays.length; i++) {
            // 해당 장르에 대한 정보가 없다면
            if(!playedCount.containsKey(genres[i])) {
                HashMap<Integer, Integer> tempMap = new HashMap<>();
                // 음악, 재생횟수
                tempMap.put(i, plays[i]);
                // 장르에 속하는 음악과 해당 음악 재생 횟수
                musicInfo.put(genres[i], tempMap);
                // 장르별 음악 재생 횟수
                playedCount.put(genres[i], plays[i]);
            } else {
                // 음악과 재생횟수 추가
                musicInfo.get(genres[i]).put(i, plays[i]);
                // 총 재생횟수 추가
                playedCount.put(genres[i], playedCount.get(genres[i]) + plays[i]);
            }
        }
        
        List<String> keyList = new ArrayList(playedCount.keySet());
        Collections.sort(keyList, (s1, s2) -> playedCount.get(s2) - (playedCount.get(s1)));
        
        for(String key : keyList) {
            HashMap<Integer, Integer> map = musicInfo.get(key);
            List<Integer> genreKey = new ArrayList(map.keySet());
            
            Collections.sort(genreKey, (s1, s2) -> map.get(s2) - (map.get(s1)));
            
            answer.add(genreKey.get(0));
            
            if(genreKey.size() > 1) {
                answer.add(genreKey.get(1));
            }
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}