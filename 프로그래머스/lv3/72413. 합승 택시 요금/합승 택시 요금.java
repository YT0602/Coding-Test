import java.util.*;

class Node implements Comparable<Node> {
        int start, end, cost;
    
        Node(int start, int end, int cost){
            this.start = start;
            this.end = end;
            this.cost = cost;
        }
    
        @Override
        public int compareTo(Node o){
            return this.cost - o.cost;
        }
    
    }

class Solution {
    static ArrayList<ArrayList<Node>> graph = new ArrayList<>();
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = Integer.MAX_VALUE;
        
        // 노드마다 간선 저장할 리스트 생성
        for (int i=0; i<=n; i++){
            graph.add(new ArrayList<>());
        }
        // 간선 추가
        for (int[] fare:fares){
            // 양방향
            graph.get(fare[0]).add(new Node(fare[0], fare[1], fare[2]));
            graph.get(fare[1]).add(new Node(fare[1], fare[0], fare[2]));
        }
        // 특정 지점에서 출발했을때 각 노드까지 비용
        int[] startA = new int[n+1];
        int[] startB = new int[n+1];
        int[] start = new int[n+1];
        
        // 최대값으로 초기화
        Arrays.fill(startA, Integer.MAX_VALUE);
        Arrays.fill(startB, Integer.MAX_VALUE);
        Arrays.fill(start, Integer.MAX_VALUE);
        
        startA = daik(a, startA);
        startB = daik(b, startB);
        start = daik(s, start);
        // s에서 i까지 합승하고 i에서 A와 B로 각각 가는 경우의 총 비용
        for (int i=1; i<=n; i++){
            answer = Math.min(answer, start[i]+startA[i]+startB[i]);
        }
        
        return answer;
    }
    public int[] daik(int s, int[] costs){
        PriorityQueue<Node> pq = new PriorityQueue<>();
        // 시작점 삽입
        pq.offer(new Node(s, s, 0));
        costs[s] = 0;
        
        while (!pq.isEmpty()){
            Node cur = pq.poll();
            int next = cur.end;
            int cost = cur.cost;
            // 방문한적 있는경우
            if (cost > costs[next]) continue;
            // 연결된 간선 목록
            ArrayList<Node> lines = graph.get(next);
            for (Node n:lines){
                int nextCost = cost + n.cost;
                // 비용이 더 적으면 갱신하고 큐에 삽입
                if (nextCost < costs[n.end]){
                    costs[n.end] = nextCost;
                    pq.offer(new Node(n.start, n.end, nextCost));
                }
            }
        }
        return costs;
    }
}