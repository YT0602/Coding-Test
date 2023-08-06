import java.io.*;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[][] arr;
	static boolean[][] visit;
	static int[] dr = {-1, 0, 1, 0};
	static int[] dc = {0, -1, 0, 1};
	
	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		
		arr = new int[N][N];
		
		int H = 0; // 최대 높이
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (arr[i][j] > H) H = arr[i][j]; // 최대 높이 갱신
			}
		}
		
		int ans = 0;
		
		for (int h=0; h<=H; h++) { // 최대 높이까지 물 높이 올리면서 탐색
			visit = new boolean[N][N];
			int cnt = 0;
			for (int i=0; i<N; i++) {
				for (int j=0; j<N; j++) {
					// 방문안했고 몰 높이보다 높이면 안전영역 탐색 시작
					if (!visit[i][j] && arr[i][j] > h) {
						DFS(i, j, h);
						cnt ++;
					}
				}
			}
			ans = Math.max(ans, cnt);
		}
		bw.write(ans + "\n");
		bw.flush();
		bw.close();
		
	}
	public static void DFS(int r, int c, int height) {
		visit[r][c] = true;
		for (int d=0; d<4; d++) {
			int nr = r + dr[d];
			int nc = c + dc[d];
			
			if (0 <= nr && nr < N && 0<= nc && nc < N) {
				// 범위 안에서, 방문 안했고 물높이보다 높은 칸이면 DFS
				if (!visit[nr][nc] && arr[nr][nc] > height) {
					DFS(nr, nc, height);
				}
			}
		}
		
	}
}