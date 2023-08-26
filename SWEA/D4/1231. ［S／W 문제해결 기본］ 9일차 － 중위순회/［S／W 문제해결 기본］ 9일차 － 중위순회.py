
import java.util.*;
import java.io.*;

class Solution
{
	static char[] arr;
	static int N;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for (int tc = 1; tc <= 10; tc++) {
			sb.append("#" + tc + " ");
			N = Integer.parseInt(br.readLine());
			// 방문 노드 알파벳 저장 배열
			arr = new char[N+1];
			
			for (int i=1; i <= N; i++) {
				// 입력 공백으로 나누고 노드번호별 알파벳 저장
				arr[i] = br.readLine().split(" ")[1].charAt(0);
			}
			// 중위순회
			DFS(1);
			sb.append("\n");
			
		}
		System.out.println(sb);
	}
	public static void DFS(int num) {
		// 트리 밖으로 나가면 리턴
		if (num > N) return;
		// 왼쪽 자식부터 탐색
		DFS(num * 2);
		// 현재노드 출력
		sb.append(arr[num]);
		// 오른쪽 자식
		DFS(num * 2 + 1);
	}
}