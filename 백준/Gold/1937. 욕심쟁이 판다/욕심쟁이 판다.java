import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, -1, 0, 1};
	static int[][] arr, dp;
	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		arr = new int[N][N];
		// 대나무 배열 입력
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		// 각 위치에서 최대 칸수 저장하는 dp배열
		dp = new int[N][N];
		// 최대 칸 수
		int ans = 0;
		for (int i=0; i<N; i++) {
			for (int j=0; j<N; j++) {
				// 모든 위치 돌면서 DFS
				ans = Math.max(ans, DFS(i, j));
			}
		}
		bw.write(ans + "\n");
		bw.flush();
		bw.close();
		
	}
	public static int DFS(int r, int c) {
		// dp값이 저장되어 있으면 바로 반환
		if (dp[r][c] != 0) return dp[r][c];
		
		dp[r][c] = 1; // 최소 1일
		for (int i=0; i<4; i++) {
			int nr = r + dx[i];
			int nc = c + dy[i];
			if (0<= nr && nr < N && 0 <= nc && nc < N) {
				// 대나무 더 많은 칸 있다면
				if (arr[r][c] < arr[nr][nc]) {
					// 현재 dp값, 다음칸에서의 최대 칸 수 +1 중 더 큰 값 저장
					dp[r][c] = Math.max(dp[r][c], DFS(nr, nc)+1);
					
				}
			}
		}
		return dp[r][c];
	}
}
