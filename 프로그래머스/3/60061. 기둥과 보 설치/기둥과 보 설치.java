import java.util.*;

class Solution {
    static boolean[][] pillar, bar;
    static int m;
    public int[][] solution(int n, int[][] build_frame) {
        List<int[]> result = new ArrayList<>();
        
        // 배열에는 기둥을 1, 보를 2로 표시
        pillar = new boolean[n+1][n+1];
        bar = new boolean[n+1][n+1];
        m = n;
        
        for (int[] frame : build_frame) {
            int x = frame[0];
            int y = frame[1];
            int a = frame[2];
            int b = frame[3];
            
            // 기둥
            if (a == 0) {
                // 설치
                if (b == 1) {
                    if (canPillar(x, y)) {
                        pillar[x][y] = true;
                    }
                } else { // 제거
                    pillar[x][y] = false;
                    if (!delete()) pillar[x][y] = true; // 삭제 안되면 복구
                }
            } else if (a == 1) { // 보
                // 설치
                if (b == 1) {
                    if (canBar(x, y)) {
                        bar[x][y] = true;
                    }
                } else { // 제거
                    bar[x][y] = false;
                    if (!delete()) bar[x][y] = true; // 삭제 안되면 복구
                }
            }
        }
        // 기둥, 보 좌표와 함께 리스트에 추가
        for (int i=0; i<=m; i++) {
            for (int j=0; j<=m; j++) {
                if (pillar[i][j]) {
                    result.add(new int[]{i, j, 0});
                }
                if (bar[i][j]) {
                    result.add(new int[]{i, j, 1});
                }
            }
        }
        // 정렬
        result.sort((a, b) -> {
                if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
                if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
                return Integer.compare(a[2], b[2]);
            });

        // 배열로 변환
        int[][] answer = result.toArray(new int[result.size()][]);
        
        return answer;
    }
    // 삭제 가능 여부 판단
    public boolean delete() {
        for (int i=0; i<=m; i++) {
            for (int j=0; j<=m; j++) {
               if (pillar[i][j] && !canPillar(i, j)) return false; // 기둥인 경우
                else if (bar[i][j] && !canBar(i, j)) return false; // 보인 경우
            }
        }
        return true;
    }
    // 기둥 설치 가능 유무
    public boolean canPillar(int x, int y) {
        // 바닥인 경우
        if (y == 0) {
            return true;
        } else if (y > 0 && pillar[x][y-1]) {
            // 기둥 위에 있는 경우
            return true;
        } else if (x > 0 && bar[x-1][y] || bar[x][y]) {
            // 보 위에 있는 경우
            return true;
        }
        return false;
    }
    // 보 설치 가능 유무
    public boolean canBar(int x, int y) {
        // 기둥에 연결된 경우
        if (y > 0 && pillar[x][y-1] || pillar[x+1][y-1] ) {
            return true;
        } else if (x > 0 && bar[x-1][y] && bar[x+1][y]) {
            // 양쪽이 보와 이어진 경우
            return true;
        }
        return false;
    }
}