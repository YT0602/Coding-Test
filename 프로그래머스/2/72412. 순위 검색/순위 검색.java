import java.util.*;

class Solution {
    Map<String, List<Integer>> infoMap = new HashMap<>();
    
    public int[] solution(String[] info, String[] query) {
        int[] answer = new int[query.length];
        
        for (String s : info) {
            String[] infoArray = s.split(" ");
            makeMap(0, infoArray, "");
        }
    
        // 이분탐색을 위해 오름차순 정렬
        for (List<Integer> list : infoMap.values()) {
            Collections.sort(list);
        }
        
        for (int i=0; i<query.length; i++) {
            // 조건과 점수 분리
            String replace = query[i].replace(" and ", "");
            String[] q = replace.split(" ");
            
            String key = q[0]; // 점수제외한 조건
            String score = q[1]; // 기준점수
            
            // 해당조건에 해당되는 점수들
            if (infoMap.get(key) == null) {
                answer[i] = 0;
            } else {
                List<Integer> scoreList = infoMap.get(key);
                // 이분탐색
                int cnt = binary(Integer.parseInt(score), scoreList);
                answer[i] = cnt;
            }
            
        }
        return answer;
    }
    
    // 이분탐색
    public int binary(int score, List<Integer> scoreList) {
        int start = 0;
        int end = scoreList.size() -1;
        
        int mid = 0;
        while (start <= end) {
            mid = (start+end)/2;
            if (scoreList.get(mid) < score) {
                start = mid+1;
            } else{
                end = mid-1;
            }
        }
        return scoreList.size()-start;
    }
    
    
    // 가능한 조합별 점수 Map 생성
    public void makeMap(int idx, String[] info, String key) {
        if (idx == 4) {
            List<Integer> score = infoMap.computeIfAbsent(key, l -> new ArrayList<Integer>());
            score.add(Integer.parseInt(info[4]));
            return;
        }
        makeMap(idx+1, info, key+"-");
        makeMap(idx+1, info, key+info[idx]);
    }
}