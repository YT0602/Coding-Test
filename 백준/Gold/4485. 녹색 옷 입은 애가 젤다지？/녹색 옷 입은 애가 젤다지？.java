import java.io.*;
import java.util.*;


public class Main {
	static int N;
	static int[][] arr, loopy;
	static boolean[][] visit;
	static int[] dx = {0, -1, 0, 1};
	static int[] dy = {-1, 0, 1, 0};
	// 가중치 비교해서 우선순위 큐에 삽입
	static class Node implements Comparable<Node>{
		int r;
		int c;
		int coin;
		
		public Node(int r, int c, int coin) {
			this.r = r;
			this.c = c;
			this.coin = coin;
		}
		@Override
		public int compareTo(Node o) {
			return Integer.compare(this.coin, o.coin);
		}
	}
	
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		// 테스트케이스
		int T = 0;
		while (true) {
			N = Integer.parseInt(bf.readLine());
			// 0이면 종료
			if(N==0) break;
			T++;
			// 지도 배열
			arr = new int[N][N];
			// 획득 루피
			loopy = new int[N][N];
			// 방문여부
			visit = new boolean[N][N];
			
			for (int i=0; i<N; i++) {
				StringTokenizer st = new StringTokenizer(bf.readLine());
				for (int j=0; j<N; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
					loopy[i][j] = Integer.MAX_VALUE;
				}
			}
			BFS();
			System.out.println("Problem " + T + ": " + loopy[N-1][N-1]);
		}
	}
	public static void BFS() {
		loopy[0][0] = arr[0][0];
		PriorityQueue<Node> q = new PriorityQueue<>();
		q.add(new Node(0, 0, arr[0][0]));
		
		while (!q.isEmpty()) {
			Node cur = q.poll();
			
			for (int i=0; i<4; i++) {
				int nr = cur.r + dx[i];
				int nc = cur.c + dy[i];
				
				if (0 <= nr && nr < N && 0 <= nc && nc < N) {
					// 다익스트라
					if (!visit[nr][nc] && loopy[nr][nc] > arr[nr][nc] + cur.coin) {
						loopy[nr][nc] = arr[nr][nc] + cur.coin;
						visit[nr][nc] = true;
						q.add(new Node(nr, nc, loopy[nr][nc]));
					}
				}
			}
		}
	}

}
