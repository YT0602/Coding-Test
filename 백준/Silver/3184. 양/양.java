import java.io.*;
import java.util.*;

public class Main {
	static int O, V, R, C;
	/*
	 * O : 전체 양 수,
	 * V : 전체 늑대 수,
	 * R : 행, C : 열
	 */
	static char[][] arr;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, -1, 0, 1};
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		arr = new char[R][C];
		for (int i=0; i<R; i++) {
			String line = bf.readLine(); // 문자열로 입력 받기
			for (int j=0; j<C; j++) {
				arr[i][j] = line.charAt(j); // 문자로 배열에 저장
			}
		}
		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) {
				// 울타리가 아니면 BFS 시작
				if (arr[i][j] != '#') {
					BFS(i, j);
				}
			}
		}
		System.out.println(O+" "+V);
	}
	// BFS
	public static void BFS(int r, int c) {
		Queue<int[]> q = new LinkedList<int[]>();
		
		int sheep = 0; // 현재 울타리 양 수
		int wolf = 0; // 현재 울타리 늑대 수
		
		q.offer(new int[] {r, c}); // 시작 위치 삽입
		// 시작 위치 양 or 늑대면 추가
		if (arr[r][c] == 'v') {
			wolf ++;
		}else if (arr[r][c] == 'o') {
			sheep ++;
		}
		// 방문 처리
		arr[r][c] = '#';
		
		while (!q.isEmpty()) {
			// 현재 위치
			int[] cur = q.poll();
			int ci = cur[0];
			int cj = cur[1];
			// 사방탐색
			for (int i = 0; i<4; i++) {
				int ni = ci + dx[i];
				int nj = cj + dy[i];
				// 다음위치가 배열 안이고, 울타리 아닐때
				if (0<= ni && ni < R && 0<= nj && nj < C) {
					if (arr[ni][nj] != '#') {
						// 큐에 위치 삽입
						q.offer(new int[] {ni, nj});
						// 양 or 늑대인 경우 추가
						if (arr[ni][nj] == 'v') {
							wolf ++;
						}else if (arr[ni][nj] == 'o') {
							sheep ++;
						}
						// 방문처리
						arr[ni][nj] = '#';
					}
				}
			}
		}
		// 해당 울타리 다 방문한 뒤, 
		// 양이 더 많으면 늑대 도망가고 양만 추가
		if (sheep > wolf) {
			O += sheep;
		// 늑대가 더 많으면 늑대 추가
		}else {
			V += wolf;
		}
	}

}
