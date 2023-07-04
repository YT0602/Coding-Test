import java.io.*;
import java.util.*;

// 가중치 비교해서 큐에 노드 삽입
class Node implements Comparable<Node>{
	int r;
	int c;
	int cost;
	public Node(int r, int c, int cost) {
		this.r = r;
		this.c = c;
		this.cost = cost;
	}
	@Override
	public int compareTo(Node o) {
		return Integer.compare(this.cost, o.cost);
	}
}

public class Main {
	static int N, M;
	static int[][] arr;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, -1, 0, 1};
	
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(bf.readLine());
		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		
		arr = new int[N][M];
		// 배열 생성
		for (int i=0; i<N; i++) {
			String line = bf.readLine();
			for (int j=0; j<M; j++) {
				arr[i][j] = line.charAt(j) - '0';
			}
		}
		// 벽 부순 횟수
		int ans = Daik(0, 0);
		System.out.println(ans);
	}
	// 다익스트라 이용한 BFS
	public static int Daik(int row, int col) {
		// 우선순위 큐(벽 부순횟수 오름차순)
		PriorityQueue<Node> q = new PriorityQueue<>();
		// 시작 위치 삽입
		q.offer(new Node(row, col, 0));
		// 방문확인 배열
		boolean[][] visit = new boolean[N][M];
		// 시작점 방문처리
		visit[row][col] = true;
		
		while (!q.isEmpty()) {
			// 현재위치
			Node cur = q.poll();
			// 도착점이면 벽 부순횟수 반환
			if (cur.r == N-1 && cur.c == M-1) {
				return cur.cost;
			}
			// 사방탐색
			for (int i=0; i<4; i++) {
				int nr = cur.r + dx[i];
				int nc = cur.c + dy[i];
				// 이동 위치가 범위 안 일 때
				if (0 <= nr && nr < N && 0 <= nc && nc < M) {
					// 벽이 아니면
					if (!visit[nr][nc] && arr[nr][nc] == 0) {
						// 방문처리하고 횟수 그대로 큐에 삽입
						visit[nr][nc] = true;
						q.offer(new Node(nr, nc, cur.cost));
					}
					// 벽이면
					if (!visit[nr][nc] && arr[nr][nc] == 1) {
						// 방문처리하고 횟수 + 1 해서 삽입
						visit[nr][nc] = true;
						q.offer(new Node(nr, nc, cur.cost+1));
						
					}
				}
			}
		}
		// 도착 못한 경우
		return 0;
	}
}
	


