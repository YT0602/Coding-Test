import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[][] jobs) {

        int n = jobs.length; // 작업 개수
        int end = 0; // 현재 시간
        int ans = 0;
        int cnt = 0; // 끝난 작업 수
        // 도착시간 기준 오름차순 정렬
        Arrays.sort(jobs, (a,b) -> a[0] - b[0]);

        // 우선순위 큐
        PriorityQueue<int[]> q = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        
        int idx = 0;
        while (cnt < jobs.length){
            // 현재 시간 이전에 도착한 작업들은 큐에 삽입
            while(idx < jobs.length && jobs[idx][0] <= end) {
                q.add(jobs[idx]);
                idx++;
            }
            // 큐에 비어있으면 
            if (q.isEmpty()){
                end = jobs[idx][0];
            } else{
                // 큐에 작업이 있으면 가장 짧은작업부터 처리
                int[] cur = q.poll();
                ans += cur[1] + end - cur[0];
                end += cur[1];
                cnt++;
            }
        }
        
        return ans/n;
    }
}