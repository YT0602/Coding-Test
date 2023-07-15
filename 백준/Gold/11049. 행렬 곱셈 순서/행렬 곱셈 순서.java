import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());
		int[][] arr = new int[N][2];
		int[][] dp = new int[N][N]; // 최소 곱셈 횟수 배열

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			arr[i][0] = Integer.parseInt(st.nextToken()); // 행
			arr[i][1] = Integer.parseInt(st.nextToken()); // 열
		}

		// 두 행렬 사이의 거리를 1부터 N-1까지 증가시키며 최소 곱셈 횟수 구하기
		for (int tmp = 1; tmp < N; tmp++) { // 행렬 사이 간격
			for (int first = 0; first + tmp < N; first++) { // 시작 행렬 번호
				dp[first][first + tmp] = Integer.MAX_VALUE;
				for (int mid = first; mid < first + tmp; mid++) { // 중간 행렬 번호
					int mul = arr[first][0] * arr[mid + 1][0] * arr[first + tmp][1];
					dp[first][first + tmp] = Math.min(dp[first][first + tmp],
							dp[first][mid] + dp[mid + 1][first + tmp] + mul);

				}
			}
		}
		int ans = dp[0][N - 1];
		bw.write(ans + "\n");
		bw.flush();
		bw.close();
	}
}
