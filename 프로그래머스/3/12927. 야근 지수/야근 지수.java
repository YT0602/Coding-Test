import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2) -> o2-o1);
        // 작업 넣고 내림차순으로 정렬
        for (int work : works) {
            pq.offer(work);
        }
        
        while (n > 0) {
            int cur = pq.poll();
            // 모든 작업 다 끝난경우
            if (cur == 0) break;
            // 가장 오래 걸리는 작업부터 한시간씩 줄여서 다시 넣기
            pq.offer(cur-1);
            n--;
        }
        // 남은 작업 계산
        while (!pq.isEmpty()) {
            int cur = pq.poll();
            if (cur == 0) break;
            answer += cur * cur;
        }
        
        return answer;
    }
}