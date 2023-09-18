import java.util.*;
import java.io.*;

class Solution {
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, -1, 0, 1};
    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        
        for (int i=0; i<5; i++){
            String[] arr = places[i];
            // 거리두기 준수 여부
            boolean tmp = true;
            // 각 칸마다 돌면서 지원자 있으면 탐색
            for (int r=0; r<5 && tmp; r++){
                for (int c=0; c<5 && tmp; c++){
                    if (arr[r].charAt(c) == 'P'){
                        // 거리두기 못 지키면 false
                        if (!check(r, c, arr)) tmp = false;
                    }
                }
            }
            
            answer[i] = tmp ? 1: 0;
        }
        return answer;
    }
    public boolean check(int r, int c, String[] map) {
        Queue<int[]> q = new LinkedList<>();
        // 시작점 추가
        q.offer(new int[] {r, c});
        
        while (!q.isEmpty()) {
            // 현재 위치
            int[] cur = q.poll();
            
            for (int i=0; i<4; i++){
                int nr = cur[0] + dr[i];
                int nc = cur[1] + dc[i];
                // 범위 체크
                if (nr < 0 || nc < 0 || nr >= 5 || nc >= 5 || (nr == r && nc == c))
                    continue;
            
                // 맨하튼 거리 계산
                int dis = Math.abs(nr - r) + Math.abs(nc - c);
                // 거리 2 안에 지원자 있는경우
                if (dis <= 2 && map[nr].charAt(nc) == 'P') {
                    return false;
                    // 빈 자리고 거리 2 이내면 계속 탐색
                } else if (dis < 2 && map[nr].charAt(nc) == 'O') {
                    q.offer(new int[] {nr, nc});
                }
            
            }
        }
        return true;
    }
}