import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(bf.readLine());
		
		StringTokenizer st = new StringTokenizer(bf.readLine());
		// 탑 정보 스택
		Stack<int[]> stack = new Stack<int[]>();
		
		for (int i=0; i<N; i++) {
			// 현재 탑 높이
			int H = Integer.parseInt(st.nextToken());
			
			while (!stack.isEmpty()) {
				// 스택 가장 위의 탑 높이가 현재보다 높거나 같으면
				if (stack.peek()[1] >= H) {
					// 거기에 부딫힘
					System.out.print(stack.peek()[0] + " ");
					break;
				}
				// 현재보다 작으면 제거
				stack.pop();
			}
			// 스택이 비어 있으면 수신 할 곳 없음
			if (stack.isEmpty()) {
				System.out.print("0" + " ");
			}
			// 현재 탑 정보 스택에 삽입
			stack.push(new int[] {i+1, H});
		}
	}
}