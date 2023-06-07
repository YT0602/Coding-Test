import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		String[] nm = bf.readLine().split(" ");
		
		int N = Integer.parseInt(nm[0]);
		int M = Integer.parseInt(nm[1]);
		
		int[][] arr = new int[N+1][M+1];
		int[][] dp = new int[N+1][M+1];
		
		for (int i=1; i<N+1; i++) {
			String[] row = bf.readLine().split(" ");
			for (int j=1; j<M+1; j++) {
				arr[i][j] = Integer.parseInt(row[j-1]);
				
			}
		}
		
		for (int i=1; i<N+1; i++) {
			for (int j=1; j<M+1; j++) {
				dp[i][j] = Math.max(arr[i][j]+dp[i-1][j], arr[i][j] + dp[i][j-1]);
				
			}
		}
		System.out.println(dp[N][M]);

	}

}
