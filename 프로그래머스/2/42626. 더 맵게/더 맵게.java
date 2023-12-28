import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> food = new PriorityQueue<>();
        
        for (int num : scoville) {
            food.offer(num);
        }
        
        while (food.peek() < K) {
            if (food.size() < 2) {
                return -1;
            }
            int first = food.poll();
            int second = food.poll();
            int newFood = first + second*2;
            food.offer(newFood);
            answer++;
        }
        
        return answer;
    }
}