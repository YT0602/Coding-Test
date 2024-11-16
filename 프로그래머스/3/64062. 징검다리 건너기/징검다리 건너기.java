import java.util.*;

class Solution {
    public int solution(int[] stones, int k) {
        int answer = 0;
        
        int min = 1;
        int max = 200_000_000;
        // 이분탐색
        while (min <= max) {
            int mid = (min+max)/2;
            
            boolean result = across(stones, k, mid);
            if (result) {
                min = mid+1;
                answer = Math.max(mid, answer);
            } else {
                max = mid - 1;
            }
        }
        return answer;
    }
    
    public boolean across(int[] stones, int k, int people) {
        int skip = 1;
        for (int num : stones) {
            // 횟수가 건널 사람보다 적으면 건너뛰는 칸 +1 
            if (num - people < 0) {
                skip++;
            // 많으면 skip 초기화
            } else {
                skip = 1;
            }
            // 최대 칸 수 넘으면 false
            if (skip > k) return false;
        }
        return true;
    }

}