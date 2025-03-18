import java.util.*;

class Solution {
    static class Robot {
        int r1;
        int c1;
        int r2;
        int c2;
        int move; // 이동횟수
        public Robot(int r1, int c1, int r2, int c2, int move) {
            this.r1 = r1;
            this.c1 = c1;
            this.r2 = r2;
            this.c2 = c2;
            this.move = move;
        }
    }
    static boolean[][][][] visited;
    static int[] moveR = {0, 1, 0, -1};
    static int[] moveC = {1, 0, -1, 0};
    public int solution(int[][] board) {
        int answer = 0;
        
        int n = board.length;
        visited = new boolean[n][n][n][n];
        
        answer = BFS(n, board);
        
        return answer;
    }
    
    public int BFS(int n, int[][] board) {
        Queue<Robot> q = new LinkedList<>();
        q.add(new Robot(0, 0, 0, 1, 0));
        
        while (!q.isEmpty()) {
            Robot cur = q.poll();
            int cr1 = cur.r1;
            int cc1 = cur.c1;
            int cr2 = cur.r2;
            int cc2 = cur.c2;
            int move = cur.move;
            
            // 범위 확인
            if (cr1 < 0 || cr1 >= n || cc1 < 0 || cc1 >= n
                || cr2 < 0 || cr2 >= n || cc2 < 0 || cc2 >= n) {
                continue;
            }
            // 벽
            if (board[cr1][cc1] == 1 || board[cr2][cc2] == 1) continue;
            // 방문 확인
            if (visited[cr1][cc1][cr2][cc2]) {
                continue;
            }
            // 도착점
            if ((cr1 == n-1 && cc1 == n-1)
                || (cr2 == n-1 && cc2 == n-1)) {
                    return move;
            }
            // 방문 처리
            visited[cr1][cc1][cr2][cc2] = true;
            visited[cr2][cc2][cr1][cc1] = true;
            // 상하좌우 이동
            for (int i=0; i<4; i++) {
                int nr1 = cr1+moveR[i];
                int nc1 = cc1+moveC[i];
                int nr2 = cr2+moveR[i];
                int nc2 = cc2+moveC[i];
                
                q.add(new Robot(nr1, nc1, nr2, nc2, move+1));
            }
            // 회전
            if (cc1 == cc2) {
                // 좌우 두칸씩 확인
                if (cc1 >=1 && board[cr1][cc1-1] == 0 && board[cr2][cc2-1] == 0) {
                    q.add(new Robot(cr1, cc1, cr1, cc1-1, move+1)); // 1번좌표 축 왼쪽 회전
                    q.add(new Robot(cr2, cc2-1, cr2, cc2, move+1)); // 2번좌표 축 왼쪽 회전
                }
                if (cc1 < n-1 && board[cr1][cc1+1] == 0 && board[cr2][cc2+1] == 0) {
                    q.add(new Robot(cr1, cc1, cr1, cc1+1, move+1)); // 1번좌표 축 오른쪽 회전
                    q.add(new Robot(cr2, cc2+1, cr2, cc2, move+1)); // 2번좌표 축 오른쪽 회전
                }
                
            } else if (cr1 == cr2) { // 가로방향이면
                // 아래 위 두칸씩 확인
                if (cr1 >=1 && board[cr1-1][cc1] == 0 && board[cr2-1][cc2] == 0) {
                    q.add(new Robot(cr1, cc1, cr1-1, cc1, move+1)); // 1번좌표 축 위 회전
                    q.add(new Robot(cr2-1, cc2, cr2, cc2, move+1)); // 2번좌표 축 위 회전
                }
                if (cr1 < n-1 && board[cr1+1][cc1] == 0 && board[cr2+1][cc2] == 0) {
                    q.add(new Robot(cr1, cc1, cr1+1, cc1, move+1)); // 1번좌표 축 아래 회전
                    q.add(new Robot(cr2+1, cc2, cr2, cc2, move+1)); // 2번좌표 축 아래 회전
                }
            }
            
        }
        return 0;
    }
}