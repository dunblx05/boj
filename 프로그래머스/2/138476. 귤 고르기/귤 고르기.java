import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        // 최종적으로 선택된 귤 종류의 수를 저장할 변수
        int answer = 0;
        
        // 1. 귤 크기별로 개수를 세기 위한 HashMap 생성
        // Key: 귤의 크기(size), Value: 해당 크기의 귤 개수(count)
        Map<Integer, Integer> map = new HashMap<>();
        
        // tangerine 배열을 순회하며 귤 크기별 개수를 계산
        for(int t : tangerine) {
            // map.getOrDefault(t, 0): t 크기의 귤이 이미 map에 있으면 그 개수를, 없으면 0을 반환
            // + 1을 하여 해당 크기의 귤 개수를 1 증가시킨 후, map에 저장
            map.put(t, map.getOrDefault(t, 0) + 1);
        }
        
        // 2. 귤의 크기(Key)들을 리스트로 변환
        // map의 value(귤의 개수)를 기준으로 정렬하기 위함
        List<Integer> keys = new ArrayList<>(map.keySet());
        
        // 3. 귤의 개수를 기준으로 내림차순 정렬
        // 개수가 많은 종류의 귤부터 선택해야 최소 종류로 k개를 채울 수 있음 (Greedy 접근)
        // o2의 개수에서 o1의 개수를 빼서 내림차순으로 정렬
        keys.sort(((o1, o2) -> map.get(o2) - map.get(o1)));
        
        // 정렬된 keys 리스트를 순회하기 위한 인덱스
        int i = 0;
        
        // 4. k개의 귤을 상자에 담는 과정
        // k가 0보다 클 동안 (즉, 아직 담아야 할 귤이 남았을 동안) 반복
        while (k > 0) {
            // 현재 가장 개수가 많은 종류의 귤을 모두 상자에 담는다
            // keys.get(i): 현재 가장 개수가 많은 귤의 크기
            // map.get(keys.get(i)): 해당 귤의 총 개수
            k -= map.get(keys.get(i));
            
            // 한 종류의 귤을 선택했으므로, answer(종류의 수)를 1 증가
            answer++;
            
            // 다음으로 개수가 많은 귤 종류를 선택하기 위해 인덱스 증가
            i++;
        }
        
        // k개를 모두 채우는 데 필요한 최소 종류의 수를 반환
        return answer;
    }
}