import java.util.*;

class Solution {
    static boolean[] visited;
    static int[][] staticQ;
    static int answer = 0;
    public int solution(int n, int[][] q, int[] ans) {
        visited = new boolean[n+1];
        staticQ = q;
        
        comb(n, 1, 0, new int[5], ans);
        return answer;
    }
    // 숫자 조합 생성
    public void comb(int n, int cur, int depth, int[] arr, int[] ans) {
        // 5개 다 차면 정답 체크
        if (depth == 5) {
            if (check(arr, ans)) answer++;
            return;
        }
        
        for (int i=cur; i<=n; i++) {
            if (!visited[i]) {
                arr[depth] = i;
                visited[i] = true;
                comb(n, i, depth+1, arr, ans);
                visited[i] = false;
            }
        }
        return;
    }
    
    public boolean check(int[] arr, int[] ans) {
        int size = ans.length;
        for (int l=0; l<size; l++) {
            int[] e = staticQ[l];
            int contain = 0; // 정답에 포함되는 숫자 개수
            
            for (int i=0; i<5; i++) {
                int target = arr[i];
                // 포함 여부 확인
                boolean flag = Arrays.stream(e)
                    .anyMatch(x -> x == target);
                if (flag) {
                    contain++;
                }
            }
            // 개수 다르면 실패
            if (contain != ans[l]) return false;
        }
        return true;
    }
}