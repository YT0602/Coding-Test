
import java.io.*;
import java.util.*;

public class Main {
	static int N, K;
	static int[] time = new int[100001]; // 이동 시간 배열
	static int[] parent = new int[100001]; // 이동 위치의 이전 위치
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		N = Integer.parseInt(st.nextToken()); // 수빈 위치
		K = Integer.parseInt(st.nextToken()); // 동생 위치
		
		BFS();
		
		// 도착점부터 반대로 탐색
		Stack<Integer> stack = new Stack<Integer>();
		int idx = K;
		// 출발점 될때까지
		while (idx != N) {
			stack.push(idx);
			idx = parent[idx];
		}
		stack.push(idx);
		// 도착 시간
		sb.append(time[K] - 1 + "\n");
		// 이동 위치들 추가
		while (!stack.isEmpty()) {
			sb.append(stack.pop() + " ");
		}
		
		System.out.println(sb);
		
		
	}
	public static void BFS() {
		Queue<Integer> q = new LinkedList<>();
		q.add(N);
		// 시작위치 초기화
		time[N] = 1;
		
		while (!q.isEmpty()) {
			int cur = q.poll();

			if (cur == K) {
				return;
			}
			for (int i=0; i<3; i++) {
				int next;
				// 이동 가능 경우의 수
				if (i == 0) {
					next = cur + 1;
				} else if (i==1) {
					next = cur - 1;
				}else {
					next = cur * 2;
				}
				// 범위 벗어나면 건너뜀
				if (next < 0 || next > 100000) continue;
				// 방문 안했던 위치면
				if (time[next] == 0) {
					// 큐에 넣고 횟수, 부모위치 저장
					q.add(next);
					time[next] = time[cur] + 1;
					parent[next] = cur;
				}
			}
		}
	}

}
