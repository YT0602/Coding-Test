import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(String[] gems) {
        int[] answer = new int[2];
        // 보석 종류
        int kind = new HashSet<>(Arrays.asList(gems)).size();
        // key : 보석종류, value : 보석 개수
        Map<String, Integer> map = new HashMap<>();
        
        int length = gems.length;
        int start = 0;
        
        if (kind == 1){
            answer[0] = 1;
            answer[1] = 1;
            return answer;
        }
        
        for (int end = 0; end < gems.length; end++){
            // 보석이 처음 나왔으면 1개, 중복이면 개수 +1
            map.put(gems[end], map.getOrDefault(gems[end], 0) + 1);
            // start번째 보석이 중복이면 하나 줄이고 시작번호 + 1
            while (map.get(gems[start]) > 1) {
                map.put(gems[start], map.get(gems[start])-1);
                start++;
            }
            // 모든 보석 다 담았고 길이 갱신 가능한경우
            if (map.size() == kind && length > (end - start)){
                length = end-start;
                answer[0] = start + 1;
                answer[1] = end + 1;
            }
        }
        
        return answer;
    }
}