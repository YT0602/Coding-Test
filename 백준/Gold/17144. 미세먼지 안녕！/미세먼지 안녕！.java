import java.io.*;
import java.util.*;

class Dust{
	int r, c, vol;
	Dust(int r, int c, int vol) {
		this.r = r;
		this.c = c;
		this.vol = vol;
	}
}
public class Main {
	static int R, C, T;
	static int[][] arr;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, -1, 0, 1};
	static Queue<Dust> q; // 먼지 정보 큐
	static int aircleaner = -1;
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(bf.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		T = Integer.parseInt(st.nextToken());
		
		arr = new int[R][C];
		for (int i=0; i<R; i++) {
			st = new StringTokenizer(bf.readLine());
			for (int j=0; j<C; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());

				// 공기청정기 열 입력
				if (arr[i][j] == -1 && aircleaner == -1) {
					aircleaner = i;
				}
			}
		}
		for (int t=0; t<T; t++) {
			// 먼지 확인하고 큐에 삽입
			check();
			// 먼지 확산
			DustMove();
			// 공기청정
			Cleaner();
		}
		int ans = 0;
		// 먼지 합산
		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) {
				if (arr[i][j] != -1) {
					ans += arr[i][j];
				}
			}
		}
		System.out.println(ans);

	}
	public static void check() {
		q = new LinkedList<Dust>();
		
		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) {
				// 먼지 위치, 양 추가
				if (arr[i][j] != -1 && arr[i][j] != 0) {
					q.add(new Dust(i, j, arr[i][j]));
				}
			}
		}
	}
	public static void DustMove() {
		while (!q.isEmpty()) {
			Dust cur = q.poll();
			if (cur.vol >= 5) {
				int new_dust = cur.vol / 5;  // 확산 먼지
				int move = 0; // 확산 수
				// 사방이동
				for (int i=0; i<4; i++) {
					int nr = cur.r + dx[i];
					int nc = cur.c + dy[i];
					// 이동 위치가 배열안에있고 공기청정기 아니면 확산
					if (0 <= nr && nr < R && 0 <= nc && nc < C) {
						if (arr[nr][nc] != -1) {
							arr[nr][nc] += new_dust;
							move++;
						}
					}
				}
				// 확산 한 만큼 먼지 감소
				arr[cur.r][cur.c] -= new_dust * move; 
			}
		}
	}
	public static void Cleaner() {
		int top = aircleaner;
		int bottom = aircleaner + 1;
		// 공기청정기 위쪽 반시계방향 순환
		// 순환 순서 반대로 입력해야함
		// 오른쪽
		for (int i=top-1; i>0; i--) {
			arr[i][0] = arr[i-1][0];
		}
		//위
		for (int i=0; i<C-1; i++) {
			arr[0][i] = arr[0][i+1];
		}
		// 왼쪽면
		for (int i=0; i<top; i++) {
			arr[i][C-1] = arr[i+1][C-1];
		}
		// 아랫면
		for (int i=C-1; i>1; i--) {
			arr[top][i] = arr[top][i-1];
		}
		// 공기청정기에서 나온 곳은 0
		arr[top][1] = 0;
		
		// 공기청정기 아래쪽 시계방향 순환
		// 오른쪽
		for (int i=bottom+1; i<R-1; i++) {
			arr[i][0] = arr[i+1][0];
		}
		// 아랫면
		for (int i=0; i<C-1; i++) {
			arr[R-1][i] = arr[R-1][i+1];
		}
		// 왼쪽면
		for (int i=R-1; i>bottom; i--) {
			arr[i][C-1] = arr[i-1][C-1];
		}
		//위
		for (int i=C-1; i>1; i--) {
			arr[bottom][i] = arr[bottom][i-1];
		}
		// 공기청정기에서 나온 곳은 0
		arr[bottom][1] = 0;
	}

}
