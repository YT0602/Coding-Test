import java.io.*;
import java.util.*;

class Point{
	int r;
	int c;
	int sea;
	public Point (int r, int c, int sea) {
		this.r = r;
		this.c = c;
		this.sea = sea;
	}
}

public class Main {
	static int N, M;
	static int[][] arr;
	static boolean[][] visit;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, -1, 0, 1};
	static Queue<Point> q = new LinkedList<>();
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		arr = new int[N][M];
		
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(bf.readLine());
			for (int j=0; j<M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int T = 0; // 녹는 시간
		// 빙하 한덩이인 동안 반복
		while (true) {
			int ice_cnt = check();
			if (ice_cnt == 0) {
				T = 0;
				break;
			} else if (ice_cnt > 1) break;
			T++;
			for (int i=0; i<N; i++) {
				for (int j=0; j<M; j++) {
					if (arr[i][j] != 0) sea_count(i, j);
				}
			}
			melt();	
		}
		System.out.println(T);
		
	}
	// 바닷물 접촉면 카운트 함수
	public static void sea_count(int r, int c) {
		int cnt = 0; // 접촉면
		
		for (int i=0; i<4; i++) {
			int nr = r + dx[i];
			int nc = c + dy[i];
			if (0 <= nr && nr < N && 0 <= nc && nc < M) {
				if (arr[nr][nc] == 0) {
					cnt++;
				}
			}
		}
		if(cnt != 0) {
			q.add(new Point(r, c, cnt)); // 좌표량 접촉면 큐에 저장
		}
	}
	// 빙하 녹이기
	public static void melt() {
		while (!q.isEmpty()) {
			Point cur = q.poll();
			// 접촉면 만큼 녹이기
			arr[cur.r][cur.c] -= cur.sea; 
			// 음수면 0으로
			if (arr[cur.r][cur.c] < 0) arr[cur.r][cur.c] = 0;
		}
	}
	// 빙하 개수 확인
	public static int check() {
		visit = new boolean[N][M];
		
		int cnt = 0;
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++) {
				if (arr[i][j] != 0 && !visit[i][j]) {
					DFS(i, j);
					cnt++;
				}
			}
		}
		return cnt;
	}
	// DFS
	public static void DFS(int r, int c) {
		visit[r][c] = true;
		
		for (int i=0; i<4; i++) {
			int nr = r + dx[i];
			int nc = c + dy[i];
			if (0 <= nr && nr < N && 0 <= nc && nc < M) {
				if (arr[nr][nc] != 0 && !visit[nr][nc]) {
					DFS(nr, nc);
				}
			}
		}
	}

}
