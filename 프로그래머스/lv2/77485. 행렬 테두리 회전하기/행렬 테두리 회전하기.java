import java.util.*;

class Solution {
    static int[][] arr;
    public int[] solution(int rows, int columns, int[][] queries) {
        int n = queries.length;
        int[] answer = new int[n];
        
        arr = new int[rows][columns];
        int num = 1;
        // 배열 만들기
        for (int i=0; i < rows; i++){
            for (int j=0; j < columns; j++){
                arr[i][j] = num;
                num++;
            }
        }
        for (int i=0; i<n; i++){
            int mn = rotation(num-1, queries[i]);
            answer[i] = mn;
        }
        
        return answer;
    }
    public int rotation(int min, int[] position) {

        int r1 = position[0] - 1;
        int c1 = position[1] - 1;
        int r2 = position[2] - 1;
        int c2 = position[3] - 1;
        int tmp = arr[r1][c1]; // 첫번째 숫자 보관
        min = Math.min(min, arr[r1][c1]);
        // 왼쪽면 이동
        for (int i=r1; i < r2; i++){
            arr[i][c1] = arr[i+1][c1];
            min = Math.min(min, arr[i][c1]);
        }
        // 아랫면 이동
        for (int i=c1; i < c2; i++){
            arr[r2][i] = arr[r2][i+1];
            min = Math.min(min, arr[r2][i]);
        }
        // 오른쪽면 이동
        for (int i=r2; i > r1; i--){
            arr[i][c2] = arr[i-1][c2];
            min = Math.min(min, arr[i][c2]);
        }
        // 윗면 이동
        for (int i=c2; i > c1; i--){
            arr[r1][i] = arr[r1][i-1];
            min = Math.min(min, arr[r1][i]);
        }
        arr[r1][c1+1] = tmp;
        return min;
        
    }
}