import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int ans = 0;
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        long total = 0; // 두 배열의 합
        long sum = 0; // q1의 합
        int limit = queue1.length + queue2.length;
        // 총합 계산하고, 배열을 큐로 옮기기
        for (int i=0; i < queue1.length; i++) {
            total += queue1[i] + queue2[i];
            sum += queue1[i];
            q1.add(queue1[i]);
            q2.add(queue2[i]);
        }
        if (total % 2 != 0) return -1; // 반으로 못 나누는 경우
        long target = total / 2; // 목표 합
        while (sum != target){
            if (ans > limit*2) return -1; // 불가능한 경우
            // q1의 합이 더 작은 경우 q2에서 빼서 q1에 넣기
            if (sum < target) {
                int cur = q2.poll();
                q1.add(cur);
                sum += cur;
                // q1이 더 크면 q1에서 빼서 q2에 넣기
            } else if (sum > target){
                int cur = q1.poll();
                q2.add(cur);
                sum -= cur;
            }
            ans++;
        }
        return ans;
    }
}