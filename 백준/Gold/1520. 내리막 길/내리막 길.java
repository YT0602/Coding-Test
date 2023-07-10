import java.io.*;
import java.util.*;

public class Main {
	static int N, M;
	static int[][] arr, dp;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, -1, 0, 1};
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		//지도 입력
		arr = new int[N][M];
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(bf.readLine());
			for (int j=0; j<M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		dp = new int[N][M]; // 각 점에서 도착점으로 가는 경로 수
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++) {
				dp[i][j] = -1;
			}
		}
		
		System.out.println(DFS(0, 0));
	}
	
	public static int DFS(int r, int c) {
		// 도착지인 경우
		if (r == N-1 && c == M-1) {
			return 1;
		}
		// 이미 방문했던 곳은 dp배열 값 반환
		if (dp[r][c] != -1) {
			return dp[r][c];
		}
		dp[r][c] = 0; // 현재 위치에서 도착점까지 경로 수 초기화
		for (int i=0; i<4; i++) {
			int nr = r + dx[i];
			int nc = c + dy[i];
			if (0 <= nr && nr < N && 0 <= nc && nc < M) {
				// 다음지점이 더 낮을때
				if (arr[r][c] > arr[nr][nc]) {
					// 다음지점에서 도착지까지 경로 수 더하기
					dp[r][c] += DFS(nr, nc);
				}
			}
		}
		return dp[r][c];
	}

}
