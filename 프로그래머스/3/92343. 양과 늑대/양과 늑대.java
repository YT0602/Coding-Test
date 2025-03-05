import java.util.*;

class Solution {
    static List<Integer>[] tree;
    static int maxSheep = 0;
    public int solution(int[] info, int[][] edges) {
        // 각 노드의 자식 노드 번호 리스트 가진 배열
        tree = new ArrayList[info.length];
        
        // 배열 초기화
        for (int i=0; i<info.length; i++) {
            tree[i] = new ArrayList<>();
        }
        // 자식 노드 추가
        for (int[] edge : edges) {
            int parent = edge[0];
            int child = edge[1];
            tree[parent].add(child);
        }
        
        // 이동가능 노드 리스트
        List<Integer> nodes = new ArrayList<>();
        nodes.add(0);
        
        // 루트노드부터 탐색
        dfs(0, 0, 0, info, nodes);
        
        return maxSheep;
    }
    
    public void dfs(int cur, int sheep, int wolf, int[] info, List<Integer> nodes) {
        // 현재 노드 카운트
        if (info[cur] == 0) {
            sheep++;
        } else {
            wolf++;
        }
        // 늑대가 양보다 많거나 같으면 돌아가기
        if (wolf >= sheep) return;
        
        // 최대값 갱신
        maxSheep = Math.max(sheep, maxSheep);
        
        // 현재 노드의 자식노드 리스트 조회
        List<Integer> childs = tree[cur];
        
        List<Integer> move = new ArrayList<>(nodes);
        move.addAll(childs);
        // 현재위치에서 양 or 늑대했다면 이동 가능 노드에서 제거
        move.remove(Integer.valueOf(cur));
        
        // 이동가능 노드 순회
        for (int node : move) {
            dfs(node, sheep, wolf, info, move);
        }
            
    }
}