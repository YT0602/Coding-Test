import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(bf.readLine());
		
		int[][] arr = new int[N][3];
		StringTokenizer st;
		// 숫자판 입력
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(bf.readLine());
			for (int j=0; j<3; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				
			}
		}
		// 최대, 최소 dp배열
		int[][] maxdp = new int[N][3];
		int[][] mindp = new int[N][3];
		// 첫줄은 그대로 입력
		for (int i=0; i<3; i++) {
			maxdp[0][i] = arr[0][i];
			mindp[0][i] = arr[0][i];
		}
		
		for (int i=1; i<N; i++) {
			// 최대점수 누적
			maxdp[i][0] = Math.max(maxdp[i-1][0], maxdp[i-1][1]) + arr[i][0];
			maxdp[i][1] = Math.max(Math.max(maxdp[i-1][0], maxdp[i-1][2]), maxdp[i-1][1]) + arr[i][1];
			maxdp[i][2] = Math.max(maxdp[i-1][2], maxdp[i-1][1]) + arr[i][2];
			// 최소점수 누적
			mindp[i][0] = Math.min(mindp[i-1][0], mindp[i-1][1]) + arr[i][0];
			mindp[i][1] = Math.min(Math.min(mindp[i-1][0], mindp[i-1][2]), mindp[i-1][1]) + arr[i][1];
			mindp[i][2] = Math.min(mindp[i-1][2], mindp[i-1][1]) + arr[i][2];
		}
		// 최대, 최소 갱신
		int mn = Integer.MAX_VALUE;
		int mx = Integer.MIN_VALUE;
		for (int i=0; i<3; i++) {
			mn = Math.min(mn, mindp[N-1][i]);
			mx = Math.max(mx, maxdp[N-1][i]);
		}
		System.out.println(mx + " " + mn);
	}

}