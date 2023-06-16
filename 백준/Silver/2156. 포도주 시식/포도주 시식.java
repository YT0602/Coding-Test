import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int[] arr = new int[N+1]; // 포도주 양
		int[] dp = new int[N+1]; // 최대 포도주
		
		for (int i=1; i<N+1; i++) {
			arr[i] = sc.nextInt();
		}
		
		dp[1] = arr[1]; // 잔이 한개 일때
		if (N>1) {
			// 잔이 두개일때
			dp[2] = arr[1]+arr[2];
		}
		for (int i=3; i<N+1; i++) {
			/*
			 * 1) OOX
			 * 2) OXO
			 * 3) XOO 
			 * 세가지 경우 중 최대값 dp 저장
			 */
			dp[i] = Math.max(dp[i-1], Math.max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i]));
		}
		System.out.println(dp[N]);
	}
}