
import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		Queue<Integer> q = new LinkedList<Integer>();

		// 사람 수만큼 번호 삽입
		for (int i = 1; i <= N; i++) {
			q.offer(i);
		}

		StringBuffer sb = new StringBuffer();
		sb.append("<");

		// 큐 크기가 1일때까지 진행
		while (q.size() > 1) {
			// K번 될때까지 맨 앞의 번호 꺼내서 맨 뒤에 다시 삽입
			for (int j = 1; j < K; j++) {
				q.offer(q.poll());
			}
			// K번째 번호
			sb.append(q.poll() + ", ");
		}
		// 마지막 번호
		sb.append(q.poll() + ">");
		
		bw.write(sb.toString() + "\n");
		bw.flush();
		bw.close();
	}
}
