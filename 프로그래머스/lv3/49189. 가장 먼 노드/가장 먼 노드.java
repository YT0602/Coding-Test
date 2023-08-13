import java.util.*;
import java.io.*;

class Solution {
    static ArrayList<Integer>[] graph;
    static int[] dis;
    public int solution(int n, int[][] edge) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int ans = 0;
        // 그래프 각 배열을 리스트로 만들기
        graph = new ArrayList[n+1];
        for (int i=1; i<=n; i++){
            graph[i] = new ArrayList<>();
        }
        // 그래프 연결
        for (int i=0; i<edge.length; i++){
            int start = edge[i][0];
            int end = edge[i][1];
            graph[start].add(end);
            graph[end].add(start);
        }
        // 거리 저장 배열
        dis = new int[n+1];
        Arrays.fill(dis, -1);
        dis[1] = 0;
        
        // BFS
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        
        while (!q.isEmpty()) {
            // 현재노드
            int cur = q.poll();
            // 현재 노드와 연결된 노드 순회
            for (int next : graph[cur]){
                if (dis[next] == -1) {
                    // 거리 갱신하고 큐에 삽입
                    dis[next] = dis[cur] + 1;
                    q.add(next);
                }
            }
        }
    
        // 가장 먼 거리
        int max_dis = Arrays.stream(dis).max().getAsInt();
        for (int x : dis){
            if(x == max_dis) ans++;
        }
        
        return ans;
    }

}