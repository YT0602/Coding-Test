import java.io.*;
import java.util.*;

class Edge implements Comparable<Edge>{
	int start;
	int end;
	double cost;
	
	Edge(int start, int end, double cost){
		this.start = start;
		this.end = end;
		this.cost = cost;
	}
	// cost기준으로 정렬
	@Override
	public int compareTo(Edge o) {
		if (this.cost > o.cost)return 1;
		return -1;
	}
}

class Point {
	int num;
	double x;
	double y;
	
	Point(int num, double x, double y) {
		this.num = num;
		this.x = x;
		this.y = y;
	}
}

public class Main {
	static int[] parent;
	static ArrayList<Edge> edgelist;
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(bf.readLine());
		Point[] p = new Point[N];
		
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(bf.readLine());
			double star_x = Double.parseDouble(st.nextToken());
			double star_y = Double.parseDouble(st.nextToken());
			
			p[i] = new Point(i, star_x, star_y);
		}
		
		edgelist = new ArrayList<Edge>();
		for (int i=0; i<N; i++) {
			for (int j=i+1; j<N; j++) {
				double cost = Math.sqrt(Math.pow(p[i].x - p[j].x, 2) + Math.pow(p[i].y - p[j].y, 2));
				edgelist.add(new Edge(p[i].num, p[j].num, cost));
			}
		}
		Collections.sort(edgelist);
		// 노드 부모를 자기 자신으로 초기화
		parent = new int[N+1];
		for (int i=0; i<N; i++) {
			parent[i] = i;
		}
		
		double ans = 0;
		// 크루스칼 알고리즘
		for (int i=0; i<edgelist.size(); i++) {
			Edge edge = edgelist.get(i);
			
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
