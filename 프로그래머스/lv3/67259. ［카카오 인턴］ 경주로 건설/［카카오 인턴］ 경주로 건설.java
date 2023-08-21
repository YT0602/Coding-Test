import java.util.*;
import java.io.*;

class Solution {
    static int[] dr = {0, -1, 0, 1};
    static int[] dc = {-1, 0, 1, 0};
    static int N, ans;
    static int[][][] visit;
    
    static class Node {
        int r, c, dir, cost;
        
        public Node (int r, int c, int dir, int cost){
            this.r = r;
            this.c = c;
            this.dir = dir;
            this.cost = cost;
        }
    }
    public int solution(int[][] board) {
        // 배열 크기
        N = board.length;
        // 방문배열
        visit = new int[N][N][4];
        ans = Integer.MAX_VALUE;

        BFS(board);
        return ans;
    }
    public void BFS(int[][] board){
        Queue<Node> q = new LinkedList<>();
        // 시작점 추가
        for (int i = 0; i < 4; i++) {
        q.add(new Node(0, 0, i, 0));
        visit[0][0][i] = 1;
        }
        
        while (!q.isEmpty()){
            Node cur = q.poll();
            // 도착점일때 비용 갱신
            if (cur.r == N-1 && cur.c == N-1){
                if(cur.cost < ans) ans = cur.cost;
                continue;
            }
            for (int d=0; d<4; d++){
                int nr = cur.r + dr[d];
                int nc = cur.c + dc[d];
                // 이동위치가 범위 안
                if (0<= nr && nr <N && 0<= nc && nc<N && board[nr][nc] == 0){
                    int nextCost = cur.cost;
                    // 방향이 안바꼈으면 + 100원
                    if (cur.dir == d){
                        nextCost += 100;
                    // 방향 바뀌면 +100 + 코너 500원
                    } else{
                        nextCost += 600;
                    }
                    // 현재좌표 현재방향 방문 안했거나 비용 더 적은 경우만 추가
                    if (visit[nr][nc][d] == 0 || visit[nr][nc][d] > nextCost) {
                        visit[nr][nc][d] = nextCost;
                        q.add(new Node(nr, nc, d, nextCost));   
                    }
                }
            }
        }
    }
}