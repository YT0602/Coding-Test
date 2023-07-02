import java.io.*;
import java.util.*;

public class Main {
	static int N, K, L;
	static int[][] arr;
	static HashMap<Integer, String> ch_dir = new HashMap<>();
	static List<int[]> snake = new ArrayList<>();
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(bf.readLine());
		K = Integer.parseInt(bf.readLine());
		arr = new int [N][N];
		
		StringTokenizer st;
		// 사과 위치 입력
		for (int i=0; i<K; i++) {
			st = new StringTokenizer(bf.readLine());
			int r = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			arr[r-1][c-1] = 1;
		}
		L = Integer.parseInt(bf.readLine());
		// 방향전환 입력
		for (int i=0; i<L; i++) {
			st = new StringTokenizer(bf.readLine());
			int time = Integer.parseInt(st.nextToken());
			String dir = st.nextToken();
			ch_dir.put(time, dir);
		}
		
		Gmae();
	}
	
	public static void Gmae() {
		int cur_r = 0; // 현재 좌표
		int cur_c = 0;
		int T = 0; // 진행 시간
		int D = 0; // 방향
		
		snake.add(new int[] {0, 0});
		
		while (true) {
			// 시간 증가
			T++;
			
			// 이동할 좌표
			int nr = cur_r + dx[D];
			int nc = cur_c + dy[D];
			
			// 종료 확인
			if (isFinish(nr, nc)) {
				break;
			}
			// 사과 먹기
			if (arr[nr][nc] == 1) {
				arr[nr][nc] = 0;
			}else { // 사과 없음
				snake.remove(0);
			}
			// 이동
			snake.add(new int[] {nr, nc});
			
			// 방향 전환
			if (ch_dir.containsKey(T)) {
				if (ch_dir.get(T).equals("D")) {
					D += 1;
					D %= 4;
				}else {
					D -= 1;
					if (D == -1) {
						D = 3;
					}
				}
			}
			// 현재 위치 업데이트
			cur_r = nr;
			cur_c = nc;
		}
		System.out.println(T);
		
	}
	public static boolean isFinish(int row, int col) {
		// 범위 밖인지 확인
		if (row < 0 || row >= N || col < 0 || col >= N) {
			return true;
		}
		// 머리가 몸에 닿는지 확인
		for (int i=0; i< snake.size(); i++) {
			int[] p = snake.get(i);
			if (row == p[0] && col == p[1]) {
				return true;
			}
		}
		return false;
	}

}
