import java.util.*;
import java.io.*;

class Solution {
    static boolean[] visit;
    static ArrayList<String> travel;
    int cnt, N;
    public String[] solution(String[][] tickets) {
        String[] answer = {};
        cnt = 0; // 사용한 항공권 수
        N = tickets.length;
        visit = new boolean[N];
        travel = new ArrayList<>(); // 전체 가능 여행 경로
        
        // 시작은 인천
        DFS("ICN", "ICN", cnt, tickets);
        
        // 오름차순 정렬
        Collections.sort(travel);
        // String 배열로 변환
        answer = travel.get(0).split(" ");
        // System.out.println(travel);
        return answer;
    }
    public void DFS(String start, String route, int cnt, String[][] tickets){
        // 항공권 모두 사용했으면 여행 경로에 추가
        if (cnt == N){
            travel.add(route);
            return;
        }
        
        for (int i=0; i<N; i++){
            // 출발지가 이전 항공권 도착지이고 사용안했으면
            if (start.equals(tickets[i][0]) && !visit[i]){
                // 방문처리하고 경로에 추가
                visit[i] = true;
                DFS(tickets[i][1], route + " " + tickets[i][1], cnt + 1, tickets);
                visit[i] = false; // 되돌리기
            }
        }
        
    }
}