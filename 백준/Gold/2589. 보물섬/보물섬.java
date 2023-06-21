import java.io.*;
import java.util.*;

public class Main {
	static int R, C;
	static char[][] arr; // 입력배열
	static int[][] visit; // 방문체크, 거리 배열
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, -1, 0, 1};
	
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(bf.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		arr = new char[R][C];
		// 배열 입력
		for (int i=0; i<R; i++) {
			String line = bf.readLine();
			for (int j=0; j<C; j++) {
				arr[i][j] = line.charAt(j);
			}
		}
		// 최대 거리
		int ans = 0;
		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) {
				// 땅이면 BFS 시작
				if (arr[i][j] == 'L') {
					visit = new int[R][C];
					int cnt = BFS(i, j);
					// 최댓값 갱신
					ans = Math.max(ans, cnt);
				}
			}
		}
		// 처음 시작이 1이었으므로 -1 
		System.out.println(ans-1);
		
	}
	public static int BFS(int r, int c) {
		Queue<int[]> q = new LinkedList<int[]>();
		// 현재 위치에서 가장 먼 거리
		int tmp = 0;
		q.offer(new int[] {r, c});
		// 방문체크
		visit[r][c] = 1;
		
		while (!q.isEmpty()) {
			int[] cur = q.poll();
			int ci = cur[0];
			int cj = cur[1];
			// 사방탐색
			for (int i=0; i<4; i++) {
				int ni = ci + dx[i];
				int nj = cj + dy[i];
				// 배열 안이고
				if (0<= ni && ni < R && 0 <= nj && nj < C) {
					// 땅이고 방문 안했으면 큐에 삽입
					if (arr[ni][nj] == 'L' && visit[ni][nj] == 0) {
						// 거리 표시
						visit[ni][nj] = visit[ci][cj] + 1;
						tmp = Math.max(tmp, visit[ni][nj]);
						q.offer(new int[] {ni, nj});
					}
				}
			}
		}

		return tmp;
	}
}