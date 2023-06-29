import java.io.*;
import java.util.*;

class Edge implements Comparable<Edge> {
	int start;
	int end;
	int cost;
	
	Edge(int start, int end, int cost) {
		this.start = start;
		this.end = end;
		this.cost = cost;
	}
	// cost 기준으로 정렬
	@Override
	public int compareTo(Edge o) {
		return this.cost - o.cost;
	}
}

public class Main {
	static ArrayList<Edge> edgeList;
	static int[] parent; // 각 노드 부모 노드 배열
	
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(bf.readLine());
		int M = Integer.parseInt(bf.readLine());
		
		edgeList = new ArrayList<>();
		
		StringTokenizer st;
		for (int i=0; i<M; i++) {
			// 시작점, 끝점, 비용 저장
			st = new StringTokenizer(bf.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());
			
			edgeList.add(new Edge(start, end, cost));
		}
		// 노드 부모를 자기 자신으로 초기화
		parent = new int[N+1];
		for (int i=1; i<=N; i++) {
			parent[i] = i;
		}
		
		Collections.sort(edgeList);
		
		int ans = 0;
		for (int i=0; i<edgeList.size(); i++) {
			Edge edge = edgeList.get(i);
			
			// 두 노드의 root가 같지 않다면, 사이클이 발생하지 않으므로 union 연산을 수행하고 비용을 더하기
			if (find(edge.start)!= find(edge.end)) {
				ans += edge.cost;
				union(edge.start, edge.end);
			}
		}
		
		System.out.println(ans);
	}
	// find 연산 x가 속한 집합의 root를 찾아 반환
	public static int find(int x) {
		if (x == parent[x]) {
			return x;
		}
		
		return parent[x] = find(parent[x]);
	}
	// union 연산 두 집합을 하나로 합치기
	public static void union(int x, int y) {
		x = find(x);
		y = find(y);
		
		if(x!=y) {
			parent[y] = x; // y의 root를 x의 root로 변경
		}
	}

}
