import java.util.*;

class Solution {
    int solution(int[][] land) {
        int answer = 0;
        int n = land.length;
        for (int i=1; i<n; i++) {
            land[i][0] += Math.max(Math.max(land[i-1][1], land[i-1][2]), land[i-1][3]);
            land[i][1] += Math.max(Math.max(land[i-1][0], land[i-1][2]), land[i-1][3]);
            land[i][2] += Math.max(Math.max(land[i-1][0], land[i-1][1]), land[i-1][3]);
            land[i][3] += Math.max(Math.max(land[i-1][0], land[i-1][1]), land[i-1][2]);
        }
        // for (int i=0; i<n; i++) {
        //     System.out.println(Arrays.toString(land[i]));
        // }
    
        answer = Arrays.stream(land[n-1]).max().getAsInt();

        return answer;
    }
}