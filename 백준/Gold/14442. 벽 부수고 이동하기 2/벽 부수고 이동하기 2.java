import java.io.*;
import java.util.*;

public class Main {
	static int N, M, K, ans;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, -1, 0, 1};
	static int[][] arr;
	static boolean[][][] visit;
	static class Node {
		int r, c, dis, wall;
		// 좌표, 이동거리, 벽 부순 횟수
		Node (int r, int c, int dis, int wall){
			this.r = r;
			this.c = c;
			this.dis = dis;
			this.wall = wall;
		}
	}
	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken()); // 행
		M = Integer.parseInt(st.nextToken()); // 열
		K = Integer.parseInt(st.nextToken()); // 벽 부수기 가능 횟수
		
		arr = new int[N][M]; // 맵
		// 방문 체크 배열 [r][c][현재 벽 부순 횟수]
		visit = new boolean[N][M][K+1];
		
		for (int i=0; i<N; i++) {
			String line = br.readLine();
			for (int j=0; j<M; j++) {
				arr[i][j] = line.charAt(j) - '0';
			}
		}
		ans = -1; // 탈출 못하면 -1 출력
		BFS();
		bw.write(ans + "\n");
		bw.flush();
		bw.close();
	}
	
	public static void BFS() {
		Queue<Node> q = new LinkedList<>();
		q.add(new Node(0, 0, 1, 0));
		visit[0][0][0] = true; // 시작점 체크
		
		while (!q.isEmpty()) {
			Node cur = q.poll();
			// 도착점이면 거리 업데이트하고 반환
			if (cur.r == N-1 && cur.c == M-1) {
				ans = cur.dis;
				return;
			}
			
			for (int i=0; i<4; i++) {
				int nr = cur.r + dx[i];
				int nc = cur.c + dy[i];
				// 이동 좌표가 범위 안이고
				if (0<= nr && nr < N && 0 <= nc && nc < M) {
					// 벽이 아니고 방문 안했으면
					if (arr[nr][nc] == 0 && !visit[nr][nc][cur.wall]) {
						// 방문 처리하고 거리 + 1해서 큐에 삽입
						visit[nr][nc][cur.wall]= true;
						q.add(new Node(nr, nc, cur.dis+1, cur.wall));
					// 벽인 경우
					} else {
						// 부술 기회가 남았고 방문 안했으면
						if (cur.wall < K && !visit[nr][nc][cur.wall+1]) {
							// 벽 부수고 이동
							visit[nr][nc][cur.wall+1] = true;
							q.add(new Node(nr, nc, cur.dis+1, cur.wall+1));
						}
					}
				}
			}
		}
	}
}
