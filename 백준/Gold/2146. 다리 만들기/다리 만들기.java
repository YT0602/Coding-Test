import java.io.*;
import java.util.*;

public class Main {
	static class Point {
		int r;
		int c;
		int cnt;

		public Point(int r, int c, int cnt) {
			this.r = r;
			this.c = c;
			this.cnt = cnt;
		}
	}

	static int N, ans;
	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = { 0, -1, 0, 1 };
	static int[][] arr;
	static boolean[][] visit;
	static ArrayList<Point> edges = new ArrayList<>(); // 섬 가장자리 좌표 리스트

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;

		N = Integer.parseInt(br.readLine());
		arr = new int[N][N];
		// 배열 입력
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		visit = new boolean[N][N];
		int num = -1; // 섬번호
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (arr[i][j] == 1 && !visit[i][j]) {
					islandNum(i, j, num);
					num--;
				}
			}
		}
		ans = Integer.MAX_VALUE;
		for (Point edge : edges) {
			BFS(edge.r, edge.c, arr[edge.r][edge.c]);
		}

		bw.write(ans + "\n");
		bw.flush();
		bw.close();

	}

	// 섬마다 번호 매기기
	public static void islandNum(int r, int c, int num) {
		arr[r][c] = num;
		visit[r][c] = true;
		Queue<Point> islandQ = new LinkedList<>();
		islandQ.add(new Point(r, c, 0));

		while (!islandQ.isEmpty()) {

			Point cur = islandQ.poll();

			for (int x = 0; x < 4; x++) {
				int nr = cur.r + dx[x];
				int nc = cur.c + dy[x];
				if (0 <= nr && nr < N && 0 <= nc && nc < N) {
					// 섬이면 번호 매기기
					if (arr[nr][nc] == 1) {
						visit[r][c] = true;
						arr[nr][nc] = num;
						islandQ.add(new Point(nr, nc, 0));
					}
					// 섬 가장자리면 좌표 리스트에 삽입
					if (arr[nr][nc] == 0) {
						if (!edges.contains(cur)) edges.add(cur);
					}
				}
			}
		}
	}
	// 최단거리 계산
	public static void BFS(int r, int c, int num) {
		visit = new boolean[N][N];
		Queue<Point> q = new LinkedList<>();
		q.add(new Point(r, c, 0)); // 좌표, 거리
		visit[r][c] = true;

		while (!q.isEmpty()) {
			Point cur = q.poll();
			
			if (cur.cnt >= ans) return;

			for (int x = 0; x < 4; x++) {
				int nr = cur.r + dx[x];
				int nc = cur.c + dy[x];
				if (0 <= nr && nr < N && 0 <= nc && nc < N) {
					// 섬 가장자리 만나면 거리 갱신
					if (arr[nr][nc] != num && arr[nr][nc] < 0) {
						ans = Math.min(ans, cur.cnt);
						return;
					}
					// 섬번호랑 다르고 바다면 거리 표시
					if (!visit[nr][nc] && arr[nr][nc] == 0) {
						visit[nr][nc] = true;
						q.add(new Point(nr, nc, cur.cnt + 1));
					}
				}
			}
		}

	}
}
