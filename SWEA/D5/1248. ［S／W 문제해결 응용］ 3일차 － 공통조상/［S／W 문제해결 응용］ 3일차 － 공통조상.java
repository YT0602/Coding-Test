
import java.util.*;
import java.io.*;

class Solution
{
	static int ans, V, E, A, B;
	static class Node {
		List<Integer> children;
		int parents;
		
		Node() {
			this.children = new ArrayList<>();
			this.parents = 0;
		}
	}
	
	static Node[] nodes;
	static ArrayList<Integer> ancestorA, ancestorB;
	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t<=T; t++) {
			st = new StringTokenizer(br.readLine());
			// 정점개수, 간선개수, 공통조상 찾을 두 노드
			V = Integer.parseInt(st.nextToken());
			E = Integer.parseInt(st.nextToken());
			A = Integer.parseInt(st.nextToken());
			B = Integer.parseInt(st.nextToken());
			nodes = new Node[V+1];
			ancestorA = new ArrayList<>(); //A의 조상
			ancestorB = new ArrayList<>(); //B의 조상
			// 노드 초기화
			for (int i=0; i < V+1; i++) {
				nodes[i] = new Node();
				
			}
			// 부모와 자식 추가
			st = new StringTokenizer(br.readLine());
			for (int i=0; i < E; i++) {
				int p = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				nodes[p].children.add(c);
				nodes[c].parents = p;
			}
			
			// A와B 공통 조상 찾기
			traverse(A, ancestorA);
			traverse(B, ancestorB);
			
			for (int i=0; i < V; i++) {
				if (!ancestorA.get(i).equals(ancestorB.get(i))) break;
				ans = ancestorA.get(i); // 공통 조상
				
			}
		int ans_size = DFS(ans);
		System.out.printf("#%d %d %d\n", t, ans, ans_size);
		}

	}
	private static void traverse(int idx, ArrayList<Integer> ancestor) {
		int parent = nodes[idx].parents;
		if (parent != 0) { //부모 노드 존재한다면
			traverse(parent, ancestor); // 조상 더 찾으러 재귀
			
		}
		ancestor.add(idx);
		
	}
	public static int DFS(int idx) { // idx 를 root로 갖는 subtree 의 크기를 계산하는 함수
		int res = 1;
		for (int child : nodes[idx].children) {
			res += DFS(child);
		}
		return res;
	}
}