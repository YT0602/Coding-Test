import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken()); // 가수 수
		int M = Integer.parseInt(st.nextToken()); // 보조 PD 수
		
		ArrayList<Integer>[] graph = new ArrayList[N+1]; // 각 가수의 뒷순서 리스트
		for (int i=0; i<=N; i++) graph[i] = new ArrayList<Integer>();
		
		int[] indegree = new int [N+1]; // 진입차수 배열
		// 보조 PD의 순서에 따라 그래프 및 진입 차수 업데이트
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int num = Integer.parseInt(st.nextToken());
			int first = Integer.parseInt(st.nextToken());
			for (int j=1; j<num; j++) {
				int next = Integer.parseInt(st.nextToken());
				graph[first].add(next);
				indegree[next]++; // 진입차수 추가
				first = next;
			}
		}
		Queue<Integer> q = new LinkedList<Integer>();
		// 진입차수 0이면 (제일 처음이면) 큐에 넣기
		for (int i=1; i<=N; i++) {
			if (indegree[i] == 0) q.add(i);
		}
		
		ArrayList<Integer> ans = new ArrayList<Integer>(); // 공연 순서 리스트
		while(!q.isEmpty()) {
			int cur = q.poll(); // 현재 공연 가수 번호
			ans.add(cur);
			for (int next : graph[cur]) {
				indegree[next]--; // 공연했으니 순서 감소
				if (indegree[next] == 0) q.add(next);
			}
		}
		// 공연 순서 정할 수 있는지 판단
		if (ans.size() != N) {
			bw.write(0 + "\n");
			bw.flush();
			
		}else {
			// 순서대로 출력
			for (int x:ans) {
				bw.write(x + "\n");
				bw.flush();
			}
		}
		bw.close();
		
	}
}
