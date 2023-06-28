import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(bf.readLine());
		
		int[] arr = new int[N];
		
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		for (int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		// 마지막에는 = 을 넣으므로 [N-1][21] 크기로 생성
		// dp[i][j]는 i번째 수까지 계산했을때 j가 되는 경우
		long[][] dp = new long[N-1][21];
		
		// 처음은 항상 1가지
		dp[0][arr[0]] = 1;
		
		// 두번째 수 부터 마지막 수 전까지 반복
		for (int i=1; i<N-1; i++) {
			// 결과값 범위 0 ~ 20
			for (int j=0; j<=20; j++) {
				// 뺄셈결과 0이상이면
				if (j-arr[i]>=0) {
					// i번째 수까지 계산했을 때 j-arr[i]가 되는 경우의 수를 추가
					dp[i][j-arr[i]] += dp[i-1][j];
				}
				// 덧셈 결과 20이하면
				if (j+arr[i] <= 20) {
					// i번째 수까지 계산했을 때 j+arr[i]가 되는 경우의 수를 추가
					dp[i][j+arr[i]] += dp[i-1][j];
				}
			}
		}
		// 마지막에 계산한 결과 값이 arr[N-1]이 되는 경우의 수를 출력
		System.out.println(dp[N-2][arr[N-1]]);
	}

}