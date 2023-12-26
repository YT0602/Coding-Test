import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        
        Arrays.sort(A);
        Arrays.sort(B);
        
        int idxA = 0;
        int idxB = 0;
        
        for (int i=0; i<A.length; i++) {
            if (A[idxA] > B[idxB] || A[idxA] == B[idxB]) {
                idxB++;
            } else {
                idxA++;
                idxB++;
                answer++;
            }
        }
        
        return answer;
    }
}