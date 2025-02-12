import java.util.*;

class Solution {
    static String[][] arr;
    static int arrR, arrC;
    static int[][] move = {{0, -1}, {-1, 0}, {1, 0}, {0, 1}};
    public int solution(String[] storage, String[] requests) {
        int answer = 0;
        
        arrR = storage.length;
        arrC = storage[0].length();
        
        // 배열 생성
        arr = new String[arrR][arrC];
        for (int i=0; i<arrR; i++) {
            for (int j=0; j<arrC; j++) {
                String row = storage[i];
                arr[i][j] = String.valueOf(row.charAt(j));
            }
        }
        // 출고 시작
        for (String target : requests) {
            if (target.length() > 1) {
                crane(target.substring(0, 1));
            } else {
                lift(target);
            }
        }
        
        // 남은 물건 카운트
        for (int i=0; i<arrR; i++) {
            for (int j=0; j<arrC; j++) {
                if (arr[i][j] != "-") {
                    answer++;
                }
            }
        }
        return answer;
    }
    
    public void lift(String target) {
        // 출고 위치 저장
        List<int[]> out = new ArrayList<>();
        
        for (int i=0; i<arrR; i++) {
            for (int j=0; j<arrC; j++) {
                // target 이면 지게차 가능한지 확인
                if (arr[i][j].equals(target)) {
                    if (check(i, j)) {
                        out.add(new int[]{i, j});
                    }
                }
            }
        }
        // 출고 표시
        for(int[] point : out) {
            int r = point[0];
            int c = point[1];
            arr[r][c] = "-";
        }
    }
    // 지게차로 뺄 수 있는지 확인
    public boolean check(int r, int c) {
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[arrR][arrC];
        
        q.add(new int[]{r, c});
        
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int cr = cur[0];
            int cc = cur[1];
            // 가장자리 확인
            if (cr == 0 || cr == arrR - 1 || cc == 0 || cc == arrC - 1) {
                return true;
            }
            
            for (int i=0; i<4; i++) {
                int nr = cr + move[i][0];
                int nc = cc + move[i][1];
                if (nr >= 0 && nr < arrR && nc >= 0 && nc < arrC && !visited[nr][nc] && arr[nr][nc].equals("-")) {
                    q.add(new int[]{nr, nc});
                    visited[nr][nc] = true;
                }
            }
        }
        return false;
    }
    
    // 크레인으로 출고
    public void crane(String target) {
        for (int i=0; i<arrR; i++) {
            for (int j=0; j<arrC; j++) {
                if (arr[i][j].equals(target)) {
                    arr[i][j] = "-";
                }
            }
        }
    }
}