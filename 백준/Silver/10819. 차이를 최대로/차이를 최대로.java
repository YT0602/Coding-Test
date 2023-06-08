import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[] numbers;
	static boolean[] visit;
	static int[] calcul;
	static int ans;
	static int N;
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(bf.readLine());
		StringTokenizer st = new StringTokenizer(bf.readLine());
		numbers = new int[N];
		visit = new boolean[N];
		calcul = new int[N];
		for (int i =0; i < N; i++) {
			numbers[i] = Integer.parseInt(st.nextToken());
		}
		DFS(0);
		System.out.println(ans);
		
	}
	
	public static void DFS(int cnt) {
		if (cnt == N) {
			int sum = 0;
			for (int i=0; i<N-1; i++) {
				sum += Math.abs(calcul[i] - calcul[i+1]);
			}
			ans = Math.max(ans, sum);
			return;
		}
		for (int i=0; i<N; i++) {
			if (!visit[i]) {
				calcul[cnt] = numbers[i];
				visit[i] = true;
				DFS(cnt+1);
				visit[i] = false;
			}
		}
	}

}
