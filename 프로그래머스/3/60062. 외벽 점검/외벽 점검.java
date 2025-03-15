import java.util.*;

class Solution {
    static int[][] weakCaseArr;
    static int answer;
    public int solution(int n, int[] weak, int[] dist) {
        // 취약점 조합
        weakCaseArr = new int[weak.length][weak.length];
        makeCase(n, weak);
        // 작업자 수
        int d = dist.length;
        answer = d+1;
        // 순열 생성
        permutation(d, 0, new int[d], dist, new boolean[d]);
        
        if (answer == d+1) answer = -1;
        return answer;
    }
    // 취약점 케이스 만들기
    public void makeCase(int n, int[] weak) {
        int l = weak.length;
        int[] weakCase;
        for (int i=0; i<l; i++) {
            weakCase = new int[l];
            // 차례대로 추가
            for (int j=i; j<l; j++) {
                weakCase[j-i] = weak[j];
            }
            // 기준점 지난 경우 둘레만큼 더하기
            for (int j=0; j<i; j++) {
                weakCase[l-i+j] = weak[j]+n;
            }
            weakCaseArr[i] = weakCase;
        }
    }
    // 작업자 순열 만들기
    public void permutation(int d, int depth, int[] cur, int[] dist, boolean[] visited) {
        if (d == depth) {
            // 각 취약지점 조합에 대해 점검
            for (int[] weakCase : weakCaseArr) {
                int cnt = check(cur, weakCase);
                if (cnt >= 0) {
                    answer = Math.min(cnt, answer);
                }
            }
            return;
        }
        for (int i=0; i<d; i++) {
            if (!visited[i]) {
                visited[i] = true;
                cur[depth] = dist[i];
                permutation(d, depth+1, cur, dist, visited);
                cur[depth] = 0;
                visited[i] = false;
            }
        }
        
    }
    // 외벽 점검
    public int check(int[] worker, int[] weakCase) {
        int idx = 0;
        int next = -1;
        for (int weak : weakCase) {
            // 점검 완료한 지점 생략
            if (weak <= next) continue;
            // 점검 못하는 경우
            if (idx >= worker.length) {
                return -1;
            }
            next = weak + worker[idx];
            idx++;
        }
        return idx;
        
    }
}