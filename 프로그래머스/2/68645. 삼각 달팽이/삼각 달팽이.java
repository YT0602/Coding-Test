import java.util.*;

class Solution {
    public int[] solution(int n) {
        int[] answer = new int[n*(n+1)/2];
        
        int[][] arr = new int[n][n];
        
        int num = 1;
        int r = -1;
        int c = 0;
        for (int i=0; i<n; i++){
            for (int j=i;j<n;j++) {
                if (i%3 == 0) { // 세로이동
                    r++;
                } else if (i%3 == 1) { // 가로이동
                    c++;
                } else { // 대각이동
                    r--;
                    c--;
                }
                arr[r][c] = num;
                num++;
            }
        }
        int idx = 0;
        for (int i=0;i<n;i++) {
            for (int j=0; j<n;j++) {
                if (arr[i][j] == 0) {
                    break;
                } else {
                    answer[idx] = arr[i][j]; 
                    idx++;
                }
            
            }
        }
        return answer;
    }
}