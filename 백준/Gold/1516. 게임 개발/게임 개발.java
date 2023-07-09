import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(bf.readLine());
		// 각 건물의 선행건물 저장할 리스트
		ArrayList<ArrayList<Integer>> list = new ArrayList<>();
		for (int i=0; i<=N; i++) {
			list.add(new ArrayList<>());
		}
		
		int[] indegree = new int[N+1]; // 각 건물의 선행 건물 개수
		int[] times = new int[N+1]; // 각 건물 짓는데 걸리는 시간
		// 건물 정보 입력
		for (int i=1; i<=N; i++) {
			st = new StringTokenizer(bf.readLine());
			times[i] = Integer.parseInt(st.nextToken());
			while (true) {
				int num = Integer.parseInt(st.nextToken());
				
				if (num == -1) break;
				
				list.get(num).add(i);
				indegree[i]++;
			}
		}
		
		Queue<Integer> q = new LinkedList<Integer>();
		int[] result = new int[N+1]; // 각 건물 완성 최소 시간
		
		for (int i=1; i<=N; i++) {
			if (indegree[i] == 0) { // 선행 건물 없는 건물부터 시작
				q.offer(i);
			}
			result[i] = times[i]; // 완성 시간 초기화
		}
		
		while (!q.isEmpty()) {
			int cur = q.poll();
			// 위상정렬
			for (int next : list.get(cur)) {
				indegree[next]--;
				result[next] = Math.max(result[next], result[cur] + times[next]);
				
				if (indegree[next] == 0) q.offer(next);
				
			}
		}
		for (int i=1; i<=N; i++) {
			System.out.println(result[i]);
		}
	}

}
