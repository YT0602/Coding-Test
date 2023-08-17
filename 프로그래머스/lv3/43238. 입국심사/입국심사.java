import java.util.*;
import java.io.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        // 심사 시간별로 오름차순 정렬
        Arrays.sort(times);
        
        long min = 1;
        // 최악의 경우 : 가장 오래 걸리는 심사 * n명
        long max = (long) times[times.length-1] * n;
        
        while (min <= max) {
            // 예상 시간
            long mid = (min+max)/2;
            long cnt = 0; // 심사 가능한 사람 수
            // 각 심사관 별로 해당 시간 안에 심사 가능한 사람 수
            for (int time : times){
                cnt += mid/time;
            }
            // 시간안에 모두 심사 가능한 경우
            if (cnt >= n){
                // 예상 시간 줄여서 다시 탐색
                max = mid -1;
                answer = mid;
            } else{
                // 시간안에 모두 불가능하면 시간 늘이기
                min = mid + 1;
            }
        }
        return answer;
    }
}