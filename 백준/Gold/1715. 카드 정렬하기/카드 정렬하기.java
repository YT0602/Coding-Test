import java.io.*;
import java.util.PriorityQueue;

public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(bf.readLine());
		// 우선순위 큐
		PriorityQueue<Integer> q = new PriorityQueue<Integer>();
		// 숫자 삽입
		for (int i=0; i<N; i++) {
			int num = Integer.parseInt(bf.readLine());
			q.add(num);
		}
		// 비교횟수
		int ans = 0;
		// 작은 수부터 빼서 더한 뒤에 다시 큐에 삽입
		while (q.size() > 1) {
			int a = q.poll();
			int b = q.poll();
			
			ans += a+b;
			q.add(a+b);
		}
		System.out.println(ans);
	}

}
