import java.io.*;
import java.util.*;

public class Main {
	static int N, M, target_x, target_y;
	static int[][] arr;
	static int[] visit;
	
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(bf.readLine());
		
		StringTokenizer st = new StringTokenizer(bf.readLine());
		target_x = Integer.parseInt(st.nextToken());
		target_y = Integer.parseInt(st.nextToken());
		
		arr = new int[N+1][N+1];
		visit = new int[N+1];
		
		M = Integer.parseInt(bf.readLine());
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(bf.readLine());
			int parent = Integer.parseInt(st.nextToken());
			int child = Integer.parseInt(st.nextToken());
			
			arr[parent][child] = 1;
			arr[child][parent] = 1;
			
		}
		BFS(target_x, target_y);
		if (visit[target_y] == 0) {
			System.out.println(-1);
		}else {
			System.out.println(visit[target_y]);
		}
	}
	private static void BFS(int x, int y) {
		Queue<Integer> q = new LinkedList<>();
		
		q.add(x);
		
		while (!q.isEmpty()) {
			int cur = q.poll();
			if (cur == y) {
				break;
			}
			for (int i=0; i<=N; i++) {
				if (arr[cur][i] == 1 && visit[i] == 0) {
					visit[i] = visit[cur] + 1;
					q.add(i);
				}
			}
			
		}
		
	}

}