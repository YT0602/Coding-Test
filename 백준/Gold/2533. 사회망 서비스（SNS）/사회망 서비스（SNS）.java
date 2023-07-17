import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static int[][] dp;
	static ArrayList<ArrayList<Integer>> sns = new ArrayList<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;

		N = Integer.parseInt(br.readLine());
		// 사용자마다 연결 리스트 추가
		for (int i = 0; i <= N; i++) {
			sns.add(new ArrayList<>());
		}
		// dp[i][j]: i번째 노드가 얼리어답터일 때(1) / 아닐 때(0)의 최소 얼리어답터 수
		dp = new int[N+1][2];
		// SNS 연결
		for (int i = 0; i < N-1; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			sns.get(a).add(b);
			sns.get(b).add(a);
		}
		DP(1, -1);

		bw.write(String.valueOf(Math.min(dp[1][0], dp[1][1])));
		bw.flush();
		bw.close();
	}

	public static void DP(int cur, int par) {
		dp[cur][0] = 0;
		dp[cur][1] = 1;
		// 현재 노드와 연결된 노드 탐색
		for (int next : sns.get(cur)) {
			// 부모노드 아니면 DP 실행
			if (next != par) {
				DP(next, cur);
				// 현재노드가 얼리어답터 아니면, 자식 노드는 얼리어답터
				dp[cur][0] += dp[next][1];
				// 현재 노드가 얼리어답터면, 자식 노드는 얼리어답터이거나 아닐 수도 있음
				dp[cur][1] += Math.min(dp[next][0], dp[next][1]);
			}
		}
	}
}
