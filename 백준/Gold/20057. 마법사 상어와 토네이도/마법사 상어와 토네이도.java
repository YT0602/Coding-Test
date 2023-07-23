import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static int[][] arr;
	static int[] dx = { 0, 1, 0, -1 };
	static int[] dy = { -1, 0, 1, 0 };
	static int[] dc = { 1, 1, 2, 2 }; // 각 방향으로 이동할 거리
	// 모래 흩어질 때 방향별 행,열 이동 좌표
	static int[][] sand_dx = { { -1, 1, -2, -1, 1, 2, -1, 1, 0 }, { -1, -1, 0, 0, 0, 0, 1, 1, 2 },
			{ 1, -1, 2, 1, -1, -2, 1, -1, 0 }, { 1, 1, 0, 0, 0, 0, -1, -1, -2 } };
	static int[][] sand_dy = { { 1, 1, 0, 0, 0, 0, -1, -1, -2 }, { -1, 1, -2, -1, 1, 2, -1, 1, 0 },
			{ -1, -1, 0, 0, 0, 0, 1, 1, 2 }, { 1, -1, 2, 1, -1, -2, 1, -1, 0 } };
	static int[] sandRatio = { 1, 1, 2, 7, 7, 2, 10, 10, 5 }; // 모래 퍼지는 퍼센트

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;

		N = Integer.parseInt(br.readLine());
		arr = new int[N][N];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		// 가운데 좌표에서 시작
		int ans = simulation(N / 2, N / 2);

		bw.write(ans + "\n");
		bw.flush();
		bw.close();

	}

	public static int simulation(int x, int y) {
		// 밖으로 나간 총 모래 양
		int total_out = 0;
		// 현재 위치
		int cur_r = x;
		int cur_c = y;

		while (true) {
			// 왼, 아래, 오른, 위쪽
			for (int i = 0; i < 4; i++) {
				// 각 방향마다 이동하는 칸 수
				for (int move = 0; move < dc[i]; move++) {
					// 이동 좌표
					int nr = cur_r + dx[i];
					int nc = cur_c + dy[i];
					// 토네이도가 밖으로 나가면 종료
					if (nr < 0 || nr >= N || nc < 0 || nc >= N) return total_out;
					// 모래 이동
					int sand = arr[nr][nc];
					arr[nr][nc] = 0;
					// 총 흩날린 양
					int total_sp = 0;
					// 9가지 방향으로 모래 흩날림
					for (int sp = 0; sp < 9; sp++) {
						int sand_r = nr + sand_dx[i][sp];
						int sand_c = nc + sand_dy[i][sp];
						int sp_sand = (sand * sandRatio[sp]) / 100;
						// 밖으로 나간 모래는 총합에 추가
						if (sand_r < 0 || sand_r >= N || sand_c < 0 || sand_c >= N) {
							total_out += sp_sand;
						} else {
							// 안나가면 배열안에 추가
							arr[sand_r][sand_c] += sp_sand;
						}
						total_sp += sp_sand;
					} 

					// 알파
					int alpha_r = nr + dx[i];
					int alpha_c = nc + dy[i];
					// 흩날리고 남은 양은 알파로 이동
					int alphaAmount  = sand - total_sp;
					// 알파도 밖으로 나가는지 확인하고 추가
					if (alpha_r < 0 || alpha_r >= N || alpha_c < 0 || alpha_c >= N) {
						total_out += alphaAmount ;
					} else {
						arr[alpha_r][alpha_c] += alphaAmount ;
					}
					// 현재 위치 변경
					cur_r = nr;
					cur_c = nc;
				}
			}
			// 방향별 이동 칸 수 업데이트
			for (int idx = 0; idx < 4; idx++) {
				dc[idx] += 2;
			}
		}
	}

}
