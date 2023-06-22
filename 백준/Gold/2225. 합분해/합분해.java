import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int K = sc.nextInt();
		
		int[][] dp = new int [N+1][K+1];
		
		// i를 1개로 만드는 경우 1가지
		for (int i=0; i<=N; i++) {
			dp[i][1] = 1;
		}
		// 1을 K개로 만드는 경우
		for (int i=0; i<=K; i++) {
			dp[1][i] = i;
		}
		// 점화식
		for (int i=2; i<=N; i++) {
			for (int j=2; j<=K; j++) {
				dp[i][j] = (dp[i-1][j]+dp[i][j-1]) % 1000000000;
			}
		}
		System.out.println(dp[N][K]);
	}

}
