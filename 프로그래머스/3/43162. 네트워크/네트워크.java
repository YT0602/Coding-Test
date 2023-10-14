class Solution {
//     DFS 풀이
    static boolean[] visit;
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visit = new boolean[n];
        
        for (int i=0; i<n; i++) {
            if (!visit[i]) {
                DFS(i, n, computers);
                answer ++;
            }
        }
        
        return answer;
    }
    public void DFS(int node, int n, int[][] computers){
        visit[node] = true;
        
        for (int i=0; i<n; i++ ) {
            if (computers[node][i]==1 && !visit[i]) {
                DFS(i, n, computers);
            }
        }
    }
    // union-find 풀이
    static int[] parent;
    public int solution2(int n, int[][] computers) {
        int answer = n;
        parent = new int[n];
        
        // 부모 초기화
        for (int i=0; i<n; i++) {
            parent[i] = i;
        }
        
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                // 연결되어있으면 union 후 차감
                if (computers[i][j] == 1) {
                    if (union(i, j)) answer --;
                }
            }
        }
        
        return answer;
    }
    // 현재노드의 루트노드 찾기
    public int find(int x) {
        // 루트가 본인인 경우
        if (x == parent[x]) {
            return x;
        }
        return parent[x] = find(parent[x]);
    }
    public boolean union(int x, int y) {
        x = find(x);
        y = find(y);
        // 루트가 다르면 y를 x의 자식으로 합치기
        if (x != y) {
            parent[y] = x;
            return true;
        }
        // 이미 같은 네트워크
        return false;
    }
}
