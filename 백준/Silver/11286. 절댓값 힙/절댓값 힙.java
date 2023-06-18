import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(bf.readLine());
		
		// 우선순위 큐
		PriorityQueue<Integer> heap = new PriorityQueue<>((o1, o2)->{
			/*
			 * o1에 높은 우선순위 주려면 -1
			 * o2에 높은 우선순위 주려면 1
			 */
			int x = Math.abs(o1);
			int y = Math.abs(o2);
			// 절댓값 같은 경우
			if (x == y) {
				// 작은 수에 우선순위
				return o1 >= o2 ? 1:-1;
			}
			// 다른 경우 절댓값 작은 수에 우선순위
			else if (x>y) {
				return 1;
			}else {
				return -1;
			}
		});
		for (int i=0; i<N; i++) {
			int num = Integer.parseInt(bf.readLine());
			
			if (num != 0) {
				// 0이 아니면 그 수 추가
				heap.add(num);
			}else {
				// 힙이 비어있으면 0 출력
				if (heap.isEmpty()) {
					System.out.println(0);
				// 비어있지 않으면 우선순위 가장 높은 값 출력
				}else {
					System.out.println(heap.poll());
				}
			}
		}
	}
}