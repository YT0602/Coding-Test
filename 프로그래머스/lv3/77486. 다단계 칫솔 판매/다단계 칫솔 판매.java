import java.util.*;

class Solution {
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        int[] answer = new int[enroll.length];
        // 자신, 부모
        Map<String, String> parentMap = new HashMap<>();
        // 자신, 순서
        Map<String, Integer> idxMap = new HashMap<>(); 
        
        for (int i=0; i<enroll.length; i++){
            parentMap.put(enroll[i], referral[i]);
            idxMap.put(enroll[i], i);
        }
        
        for (int i=0; i<seller.length; i++){
            String cur = seller[i];
            int profit = 100 * amount[i];
            // root 나올때까지 반복
            while (!cur.equals("-")){
                // 넘겨줄 금액
                int parentProfit = profit / 10;
                // 자기가 가져갈 금액
                int myProfit = profit - parentProfit;
                // 자기 순서에 금액 추가
                answer[idxMap.get(cur)] += myProfit;
                
                // 부모로 이동
                cur = parentMap.get(cur);
                profit /= 10;
                // 넘겨줄 금액 없으면 중단
                if (profit == 0) break;
            }
        }
        return answer;
    }
}