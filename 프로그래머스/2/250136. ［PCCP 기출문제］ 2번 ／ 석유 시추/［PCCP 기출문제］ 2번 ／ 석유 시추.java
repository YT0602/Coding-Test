import java.util.*;

class Solution {
    int[] moveR = {-1, 0, 1, 0};
    int[] moveC = {0, -1, 0, 1};
    int[] memo; // 각 열의 석유량에 대해 메모이제이션
    public int solution(int[][] land) {
        int answer = 0;
        
        int x = land.length; // 행 수
        int y = land[0].length; // 열 수
        
        boolean[][] visited = new boolean[x][y];
        
        memo = new int[y];
        for (int i=0; i<x; i++) {
            for (int j=0; j<y; j++) {
                if (land[i][j] == 1 && !visited[i][j]) {
                    bfs(land, visited, i, j);
                }
            }
        }
        // 최대값 찾기
        for (int oil : memo) {
            answer = Math.max(oil, answer);
        }
        
        
        return answer;
    }
    // BFS
    public void bfs(int[][] land, boolean[][] visited, int r, int c) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{r, c});
        visited[r][c] = true;
        
        int oil = 1;
        Set<Integer> set = new HashSet<>();
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int cr = cur[0];
            int cc = cur[1];
            set.add(cc);
            
            for (int i=0; i<4; i++) {
                int nr = cr + moveR[i];
                int nc = cc + moveC[i];
                
                // 범위 벗어나면 pass
                if (nr < 0 || nr >= land.length || nc < 0 || nc >= land[0].length) {
                    continue;
                }
                // 시추안한 석유있으면 큐에 추가하고 석유량 추가
                if (!visited[nr][nc] && land[nr][nc] == 1) {
                    visited[nr][nc] = true;
                    oil++;
                    q.add(new int[]{nr, nc});
                }
            }
        }
        // 지나간 열에 대해 시추한 덩어리 양 추가
        for (int col : set) {
            memo[col] += oil;
        }
    }
    
}