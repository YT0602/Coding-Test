import java.util.*;

class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        Queue<Integer> tmpServer = new LinkedList<>();
        
        int maxPlayer = m; // 서버 증설 고려한 최대 사용자 수
        for (int i=0; i<24; i++) {
            int curPlayer = players[i];
            int cnt = 0; // 현재 해야하는 서버 증설 횟수
            
            if (curPlayer >= maxPlayer) {
                cnt += (curPlayer-maxPlayer)/m+1;
                // k시간 동안 유지되는 증설 서버 추가
                for (int j=0; j<cnt; j++) {
                    tmpServer.add(k);
                }
                maxPlayer += m*cnt; // 최대 사용자 수 추가
                answer += cnt; // 서버 증설 횟수 추가
            }
            // 시간 감소
            int size = tmpServer.size();
            for (int j=0; j<size; j++) {
                int time = tmpServer.poll();
                time--;
                // 시간 남아있으면 다시 넣기
                if (time > 0) {
                    tmpServer.add(time);
                } else {
                    maxPlayer -= m; // 서버 시간 끝나면 사용자수 다시 차감
                }
                
            }
        }
        return answer;
    }
}