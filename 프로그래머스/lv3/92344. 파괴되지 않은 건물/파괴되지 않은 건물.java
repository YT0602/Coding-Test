import java.util.*;

class Solution {
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        // 누적합 배열
        int[][] dp = new int[board.length+1][board[0].length+1];
        
        // 스킬 사용
        for (int[] s : skill) {
            int add;
            if (s[0] == 1) {
                add = -s[5];
            } else {
                add = s[5];
            }
            /**
            * (r1, c1)에 +add
            * (r1, c2+1)에 -add
            * (r2+1, c1)에 -add
            * (r2+1, c2+1)에 +add
            */
            dp[s[1]][s[2]] += add;
            dp[s[1]][s[4]+1] -= add;
            dp[s[3]+1][s[2]] -= add;
            dp[s[3]+1][s[4]+1] += add;
        }
        // 누적합 계산하고 board에 적용
        for (int r = 0; r < board.length; r++){
            for (int c = 0; c < board[0].length; c++){
                // 첫 행 또는 열이면 그대로 적용
                if (r > 0) dp[r][c] += dp[r-1][c];
                if (c > 0) dp[r][c] += dp[r][c-1];
                // 중복 제거
                if (r > 0 && c > 0) dp[r][c] -= dp[r-1][c-1];
                
                board[r][c] += dp[r][c];
                // 건물 파괴안됐으면 추가
                if (board[r][c] > 0) answer++;
            }
        }
        
        return answer;
    }
}