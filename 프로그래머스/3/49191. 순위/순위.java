import java.util.*;


class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        int[][] floyd = new int[n+1][n+1];
        
        for (int i=0; i<results.length; i++) {
            int winner = results[i][0];
            int loser = results[i][1];
            floyd[winner][loser] = 1; // 이겼을때 1로 표시
            floyd[loser][winner] = -1; // 졌을때 -1로 표시
        }
        
        // 플로이드 워셜
        // i -> k, k -> j 면 i -> j or i <- k, k <- j 면 i <- j
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=n; j++) {
                for (int k=1; k<=n; k++) {
                    if (floyd[i][k] == 1 && floyd[k][j] == 1) {
                        floyd[i][j] = 1;
                        floyd[j][i] = -1;
                    }
                    if (floyd[i][k] == -1 && floyd[k][j] == -1) {
                        floyd[i][j] = -1;
                        floyd[j][i] = 1;
                    }
                }
            }
        }
        
        for (int i=1; i<=n; i++) {
            int cnt = 0;
            for (int j=1; j<=n; j++) {
                if (floyd[i][j] != 0) cnt++;
            }
            if (cnt == n-1) answer++;
        }
        
        return answer;
    }
}

// 기존풀이(시간초과)
class Solution2 {
    static Set<Integer> cnt;
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        ArrayList<Integer>[] myLoser = new ArrayList[n+1]; // 각 선수별 본인이 이긴 선수번호 리스트
        ArrayList<Integer>[] myWinner = new ArrayList[n+1]; // 각 선수별 본인을 이긴 선수 번호 리스트
        for (int i=0; i<=n; i++) {
            myLoser[i] = new ArrayList<>();
            myWinner[i] = new ArrayList<>();
        }
        
        for (int[] fight : results) {
            int winner = fight[0];
            int loser = fight[1];
            myLoser[winner].add(loser);
            myWinner[loser].add(winner);
        }
        // System.out.println(Arrays.toString(myLoser));
        // System.out.println(Arrays.toString(myWinner));
        
        for (int i=1; i<=n; i++) {
            cnt = new HashSet<>();
            countPlayer(myLoser, i);
            countPlayer(myWinner, i);
            if (cnt.size() == n-1) answer++;
            // else System.out.println(i+"번 실패");
        }
        
        return answer;
    }
    
    public void countPlayer(ArrayList<Integer>[] list, int n) {
        if (list[n].size() > 0) {
            for (int next : list[n]) {
                cnt.add(next);
                // System.out.println("num : "+ n);
                // System.out.println("set : "+ cnt);
                countPlayer(list, next);
            }
            return;
        } else {
            return;
        }
    }
}