import java.util.*;

class Solution {
    static int INF = 1_000_000;
    public int solution(int[][] info, int n, int m) {
        int answer = INF;
        
        int l = info.length;
        // i번째 물건에서 B흔적이 j일때 A의 흔적 배열
        int[][] dp = new int[l+1][m];
        // 기본값 초기화
        for (int i=0; i<=l; i++) {
            Arrays.fill(dp[i], INF);
        }
        
        dp[0][0] = 0;
        for (int i=1; i<=l; i++) {
            int a = info[i-1][0];
            int b = info[i-1][1];
            for (int j=0; j<m; j++) {
                // a가 물건 훔친 경우
                // b의 흔적은 그대로, a의 흔적만 추가
                dp[i][j] = Math.min(dp[i][j], dp[i-1][j]+a);
                // b가 물건 훔친 경우
                // b가 훔칠 수 있는 경우 한정, b의 흔적을 이전 흔적에 추가, a의 흔적은 그대로
                if (j+b < m) {
                    dp[i][j+b] = Math.min(dp[i][j]+b, dp[i-1][j]);
                }
            }
        }
        // 최솟값 찾기
        for (int j=0; j<m; j++) {
            answer = Math.min(dp[l][j], answer);
        }
        
        // A 붙잡히는 경우
        if (answer >= n) answer = -1;
        return answer;
    }
}