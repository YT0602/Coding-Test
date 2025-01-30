import java.util.*;

class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        
        int deliverCount = 0; // 배달한 물건 수
        int pickupCount = 0; // 픽업한 물건 수
        
        for (int i=n-1; i>=0; i--) {
            deliverCount += deliveries[i];
            pickupCount += pickups[i];
            // 카운트가 0보다 크다면 배달 or 픽업 하러 그만큼 이동해야 한다는 의미
            // 해당 집의 카운트를 더해도 0보다 작다면 해당 집은 이전에 이동할때 처리되었다고 판단 == 이동 필요 없음
            while (deliverCount > 0 || pickupCount > 0) {
                deliverCount -= cap;
                pickupCount -= cap; // 한번 이동하면 최대로 배달 or 수거
                answer += (i+1)*2; // 왕복 거리만큼 이동
            }
        }
        return answer;
    }
    
}