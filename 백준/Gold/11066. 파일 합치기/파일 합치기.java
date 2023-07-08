import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int T=  Integer.parseInt(bf.readLine());
		for (int tc=0; tc<T; tc++) {
			int N = Integer.parseInt(bf.readLine());
			// 파일 크기 배열
			int[] arr = new int [N+1];
			// 누적합
			int[] sum = new int[N+1];
			// DP
			int[][] dp = new int[N+1][N+1];
			
			StringTokenizer st = new StringTokenizer(bf.readLine());
			for (int i=1; i<=N; i++) {
				// 파일 크기, 누적합 입력
				arr[i] = Integer.parseInt(st.nextToken());
				sum[i] = sum[i-1] + arr[i];
			}
			
			for (int k=1; k<=N; k++) {
				// dp[i][j]는 i번째 파일부터 j번째 파일까지 합치는데 필요한 최소 비용
				for (int i=1; i+k <= N; i++) {
					int j = i+k;
					dp[i][j] = Integer.MAX_VALUE;
					for (int m = i; m<j; m++) {
						/*
						 * dp[i][m] = i부터 m까지 합치는 비용
						 * dp[m+1][j] = m+1부터 j까지 합치는 비용
						 * sum[j] - sum[i-1] = i부터 j 까지 파일 크기 합
						 * == 합치는 비용이 중복으로 쌓이므로 한번 더 더해줌
						 */
						dp[i][j] = Math.min(dp[i][j], dp[i][m] + dp[m+1][j] + sum[j] - sum[i-1]);
					}
				}
			}
			System.out.println(dp[1][N]);
		}
	}

}
