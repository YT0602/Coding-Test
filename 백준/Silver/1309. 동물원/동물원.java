import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int[][] dp = new int[N][3];
		/*
		 * DP 테이블 초기화, 2차원 배열 dp[N][3]
		 * 0: 사자가 없는 경우, 1: 왼쪽에 사자가 있는 경우, 2: 오른쪽에 사자가 있는 경우
		 */
		Arrays.fill(dp[0],1);
		// 1열은 사자가 없거나 왼쪽, 오른쪽에만 있을 수 있으므로 1로 초기화
		
		for (int i=1; i<N; i++) {
			dp[i][0] = (dp[i-1][0]+dp[i-1][1]+dp[i-1][2]) % 9901;
			// 현재 우리에 사자가 없는 경우, 이전 우리에 사자가 없거나 왼쪽, 오른쪽에 있는 경우의 수의 합
			dp[i][1] = (dp[i-1][0]+dp[i-1][2]) % 9901;
			// 현재 우리의 왼쪽에 사자가 있는 경우, 이전 우리에 사자가 없거나 오른쪽에 있는 경우의 수의 합
			dp[i][2] = (dp[i-1][0]+dp[i-1][1]) % 9901;
			// 현재 우리의 오른쪽에 사자가 있는 경우, 이전 우리에 사자가 없거나 왼쪽에 있는 경우의 수의 합

		}
		
		int ans = (dp[N-1][0]+dp[N-1][1]+dp[N-1][2]) % 9901;
		System.out.println(ans);
	}
}