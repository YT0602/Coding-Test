import java.util.*;

class Solution {
    static Map<String, Integer> map = new HashMap<>();
    
    public String[] solution(String[] orders, int[] course) {
        List<String> answer = new ArrayList<>();
        
        for (String order : orders) {
            // 매뉴 리스트로 나눠서 오름차순 정렬
            char[] arr = order.toCharArray();
            Arrays.sort(arr);
            // 가능한 메뉴조합
            combi(arr, 0, new StringBuilder());
        }
        
        for (int num : course) {
            PriorityQueue<Map.Entry<String, Integer>> pq = new PriorityQueue<>((a,b) -> b.getValue() - a.getValue());
            // course와 메뉴 수 같은거만 추가
            for (Map.Entry<String, Integer> entry : map.entrySet()) {
                if(entry.getKey().length() == num){
                    pq.offer(entry);
                }
            }
            int max = 0;
            while (!pq.isEmpty()) {
                Map.Entry<String, Integer> entry = pq.poll();
                // 두명이상이 주문했고 최대면 추가
                if (entry.getValue() >= 2 && (max == 0 || max == entry.getValue())) {
                    max = entry.getValue();
                    answer.add(entry.getKey());
                } else {
                    break;
                }
            }
        }
        // 알파벳순 정렬
        Collections.sort(answer);
        return answer.toArray(new String[0]);
    }
    public void combi(char[] arr, int start, StringBuilder sb) {
        // 두개 이상이면 초기화 or 카운트
        if (sb.length() > 1) {
            map.put(sb.toString(), map.getOrDefault(sb.toString(), 0) + 1);
        }
        // 재귀로 조합
        for (int i=start; i<arr.length; i++) {
            sb.append(arr[i]);
            combi(arr, i+1, sb);
            // 마지막꺼 제거
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}