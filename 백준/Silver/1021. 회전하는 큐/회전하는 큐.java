import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(bf.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		LinkedList<Integer> deque = new LinkedList<Integer>();
		// 회전 수
		int cnt = 0;
		// 덱에 차례대로 숫자 추가
		for (int i=1; i<=N; i++) {
			deque.add(i);
			
		}
		// 뽑을 수 담을 배열
		int[] arr = new int[M];
		st = new StringTokenizer(bf.readLine()," ");
		for ( int i=0; i<M; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			
		}
		
		for (int i=0; i<M; i++) {
			// 뽑을 수의 인덱스
			int idx = deque.indexOf(arr[i]);
			// 인덱스가 배열 사이즈 반 이하면 2번
			if (idx <= deque.size()/2) {
				for (int j=0; j<idx; j++) {
					int temp = deque.poll();
					deque.add(temp);
					cnt++;
				}
			}
			// 반 초과면 3번 실행
			else {
				for(int j=0; j<deque.size()-idx; j++) {
					int temp = deque.pollLast();
					deque.addFirst(temp);
					cnt++;
				}
			}
			deque.poll();
		}
		System.out.println(cnt);
	}
}