import java.util.*;
import java.io.*;

class Solution
{
	static int[][] arr;
	static int ans, N;
	static int[] dr = {-1, -1, 0, 1, 1, 1, 0, -1};
	static int[] dc = {0, 1, 1, 1, 0, -1, -1, -1};
	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t <= T; t++) {
			N = Integer.parseInt(br.readLine());
			arr = new int[N][N];
			ans = 0; // 클릭 수
			// 지뢰면 -2, 없으면 -1
			for (int i=0; i < N; i++) {
				String str = br.readLine();
				for (int j=0; j < N; j++) {
					if (str.charAt(j) == '.') arr[i][j] = -1;
					else arr[i][j] = -2;
				}
			}
			// 지뢰찾기
			solve();
			System.out.println("#" + t + " " + ans);
		}
	}
	public static void solve() {
		for (int i=0; i < N; i++) {
			for (int j=0; j < N; j++) {
				if (arr[i][j] != -1) continue;
				// 지뢰 아니면 주변탐색
				if (isZero(i, j)) {
					// 주변에도 지뢰없으면 클릭
					click(i, j);
					ans ++;
				}
			}
		}
		// 아직 클릭되지 않은 칸 클릭
		for (int i=0; i < N; i++) {
			for (int j=0; j < N; j++) {
				if (arr[i][j] == -1) ans ++;
			}
		}
	}
	public static boolean isZero(int r, int c) {
		// 팔방탐색하면서 지뢰찾기
		for (int i=0; i < 8; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];
			// 지뢰면 false
			if (0 <= nr && nr < N && 0 <= nc && nc < N) {
				if (arr[nr][nc] == -2) return false;
			}
		}
		return true;
	}
	public static void click(int r, int c) {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] {r, c});
		// 클릭칸 주변에는 지뢰 없음
		arr[r][c] = 0;
		while (!q.isEmpty()) {
			int[] cur = q.poll();
			arr[cur[0]][cur[1]] = 0;
			
			for (int i=0; i < 8; i++) {
				int nr = cur[0] + dr[i];
				int nc = cur[1] + dc[i];
				if (0 <= nr && nr < N && 0 <= nc && nc < N && arr[nr][nc] == -1) {
					// 클릭한 칸에서 팔방탐색하면서 주변 칸도 클릭 가능한지 확인
					if (isZero(nr, nc)) {
						q.add(new int[] {nr, nc});
					}
					arr[nr][nc] = 0;
				}
			}
		}
	}
}