import java.util.*;
import java.io.*;

class Solution {
    static int[] parent;
    public int solution(int n, int[][] costs) {
        int ans = 0;
        
        // 정렬
        Arrays.sort(costs, (o1, o2) -> o1[2] - o2[2]);
        
        parent = new int[n+1]; // 각 노드의 부모노드 배열
        // 자기 자신으로 초기화
        for (int i=0; i<n; i++){
            parent[i] = i;
        }
        // 크루스칼 알고리즘
        for (int i=0; i<costs.length; i++){
            int cur = costs[i][0];
            int next = costs[i][1];
            int cost = costs[i][2];
            // 두 노드의 root가 다르면 사이클이 발생하지 않으므로 union연산
            if (find(cur) != find(next)) {
                ans += cost;
                union(cur, next);
            }
        }
        return ans;
    }
    // x가 속한 집합의 root를 찾아 반환
    public int find(int x){
        if(x == parent[x]){
            return x;
        }
        return parent[x] = find(parent[x]);
    }
    // 연산 두 집합을 하나로 합치기
    public void union(int x, int y){
        x = find(x);
        y = find(y);
        // 두 노드의 root가 다르면 합치기
        if (x != y){
            parent[y] = x; // y의 root를 x의 root로 변경
        }
    }
}