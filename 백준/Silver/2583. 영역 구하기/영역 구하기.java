import java.io.*;
import java.util.*;

public class Main {
	static int[][] arr;
	static int M, N;
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(bf.readLine());
		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		arr = new int[M][N];
		
		// 사각형 위치 표시
		for (int i=0; i<K; i++) {
			st = new StringTokenizer(bf.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			for (int r=y1; r<y2; r++) {
				for (int c=x1; c<x2; c++) {
					arr[r][c] = 1;
				}
			}
		}
		// 영역 담을 배열
		ArrayList<Integer> lst = new ArrayList<Integer>();
		// 0이면 BFS 시작
		for (int i=0; i<M; i++) {
			for (int j=0; j<N; j++) {
				if (arr[i][j] == 0) {
					int map = BFS(i, j);
					// 영역크기 추가
					lst.add(map);
				}
			}
		}
		// 오름차순
		Collections.sort(lst);
		int ans = lst.size();
		
		System.out.println(ans);
		for (int x:lst) {
			System.out.print(x + " ");
		}
		
	}
	// BFS 함수
	public static int BFS(int row, int col) {
		Queue<int[]> q = new LinkedList<int[]>();
		// 처음 위치 큐에 추가하고 방문표시
		q.offer(new int[] {row, col});
		arr[row][col] = 1;
		// 영역 크기 변수
		int cnt = 1;
		
		int[] dx = {-1, 0, 1, 0};
		int[] dy = {0, -1, 0, 1};
		
		while (!q.isEmpty()) {
			int[] cur = q.poll();
			// 현재 위치
			int cur_r = cur[0];
			int cur_c = cur[1];
			//사방탐색
			for (int i=0; i<4; i++) {
				int nr = cur_r + dx[i];
				int nc = cur_c + dy[i];
				// 범위 안이고 방문 안했다면
				if (0 <= nr && nr < M && 0 <= nc && nc < N) {
					if (arr[nr][nc] == 0) {
						// 표시하고 큐에 추가
						arr[nr][nc] = 1;
						cnt ++;
						q.offer(new int[] {nr, nc});
					}
				}
			}
		}
		return cnt;
		
	}
}