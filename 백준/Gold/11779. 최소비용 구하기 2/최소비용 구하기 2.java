import java.io.*;
import java.util.*;

public class Main {
	static int N, M;
	static int[] dist, last;
	static ArrayList<Node>[] graph;
	static class Node implements Comparable<Node> {
		int end;
		int cost;
		public Node(int end, int cost) {
			this.end = end;
			this.cost = cost;
		}
		@Override
		public int compareTo(Node o) {
			return this.cost - o.cost;
		}
	}
	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		// 도시 수만큼 리스트 생성
		graph = new ArrayList[N+1];
		for (int i=1; i<=N; i++) {
			graph[i] = new ArrayList<>();
		}
		// 노드 연결
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int S = Integer.parseInt(st.nextToken());
			int E = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());
			graph[S].add(new Node(E, cost));
		}
		// 최종 출발, 도착점
		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		int end = Integer.parseInt(st.nextToken());
		
		dist = new int[N+1];
		last = new int[N+1];

		Arrays.fill(dist, Integer.MAX_VALUE);
		daik(start);
		// 최단거리 출력
		bw.write(dist[end] + "\n");
		bw.flush();
		// 경로를 스택에 기록
		Stack<Integer> stack = new Stack<Integer>();
		stack.push(end);
		while (last[end] != 0) {
			stack.push(last[end]);
			end = last[end];
		}
		bw.write(stack.size() + "\n"); // 경로 도시 수 출력
		bw.flush();
		// 경로 출력
		while (!stack.isEmpty()) {
			bw.write(stack.pop() + " ");
		}
		bw.flush();
		bw.close();
		
	}
	public static void daik(int start) {
		PriorityQueue<Node> q = new PriorityQueue<>();
		q.add(new Node(start, 0)); // 시작노드 추가
		dist[start] = 0;
		last[start] = 0;
		
		while (!q.isEmpty()) {
			Node curNode = q.poll();
			int cur = curNode.end;
			// 방문한적 있으면 패스
			if (dist[cur] < curNode.cost) continue;
			
			for (Node next : graph[cur]) {
				int target = next.end; // 다음 도시
				// 최단거리 갱신
				if (dist[target] > dist[cur] + next.cost) {
					dist[target] = dist[cur] + next.cost;
					last[target] = cur; // 이전마을 기록
					q.add(new Node(target, dist[target]));
				}
			}
		}
	}
}
