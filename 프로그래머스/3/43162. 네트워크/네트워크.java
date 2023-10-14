class Solution {
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
}