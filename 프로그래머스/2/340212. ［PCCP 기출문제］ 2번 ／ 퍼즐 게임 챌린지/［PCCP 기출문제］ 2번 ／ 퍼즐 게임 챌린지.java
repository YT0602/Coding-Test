import java.util.*;

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int answer = 0;
        
        int low = 1;
        int high = 100_000;
        // 이분탐색
        while (low <= high) {
            int mid = (low+high)/2;
            long result = puzzle(mid, diffs, times);
            
            // limit보다 적게 걸렸으면 숙련도 감소
            if (result < limit) {
                answer = mid; // 현재 숙련도가 최소 숙련도
                high = mid-1;
            } else if (result == limit) {
                answer = mid;
                break;
            } else { // 더 걸렸으면 숙련도 증가
                low = mid+1;
            }
        }
        return answer;
    }
    // 퍼즐 풀기
    public long puzzle(int level, int[] diffs, int[] times) {
        long result = 0;
        
        result += times[0]; // 첫 퍼즐은 항상 난이도 1
        for (int i=1; i<diffs.length; i++) {
            if (diffs[i] > level) {
                // n번 틀린 후 현재 퍼즐 풀기
                result += (diffs[i]-level) * (times[i]+times[i-1]);
                result += times[i];
            } else {
                result += times[i];
            }
        }
        return result;
    }
}