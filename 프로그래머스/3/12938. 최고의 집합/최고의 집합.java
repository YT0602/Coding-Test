import java.util.*;

class Solution {
    public int[] solution(int n, int s) {
        int[] answer = new int[n];
        
        if (n > s) {
            return new int[] {-1};
        }
        
        for (int i=0; i<n; i++) {
            answer[i] = s/n;
        }
        
        int idx = n-1;
        for (int i=0; i<s%n; i++) {
            answer[idx]++;
            idx--;
        }
        
        return answer;
    }
}