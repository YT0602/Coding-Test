import java.io.*;
import java.util.*;

class Solution {
	static int N;
	static ArrayList<Integer> list;
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		for (int t = 1; t <= 10; t++) {
			// 암호문 개수
			N = Integer.parseInt(br.readLine());
			// 암호문 리스트
			list = new ArrayList<>();

			st = new StringTokenizer(br.readLine());
			// 원본 암호문 입력
			for (int i = 0; i < N; i++) {
				list.add(Integer.parseInt(st.nextToken()));
			}
			// 명령어 개수
			int M = Integer.parseInt(br.readLine());

			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < M; i++) {
				// 명령어
				char cmd = st.nextToken().charAt(0);
				int x = Integer.parseInt(st.nextToken());
				func(cmd, x);
			}
			sb.append("#" + t);
			for (int i=0; i<10; i++) {
				sb.append(" " + list.get(i));
			}
			sb.append("\n");
		}
		bw.write(sb + "\n");
		bw.flush();
		bw.close();
		br.close();

	}

	public static void func(char cmd, int x) {
		int y;
		switch (cmd) {
		case 'I':
			// 삽입인 경우 y입력받기
			y = Integer.parseInt(st.nextToken());
			// 삽입 위치 x 에 암호문 입력
			for (int i = 0, insertIdx = x; i < y; i++, insertIdx++) {
				list.add(insertIdx, Integer.parseInt(st.nextToken()));
			}
			break;
		case 'D':
			// 삭제인 경우 y 입력받기
			y = Integer.parseInt(st.nextToken());
			for (int i = 0; i < y; i++) {
				// x번째 암호문 삭제 (삭제되면 인덱스 당겨지기 때문에 x 변경 할 필요 없음)
				list.remove(x);
			}
			break;
		case 'A':
			// 추가인 경우 y를 x로 취급, 맨뒤에 추가하므로 인덱스 필요없음
			for (int i=0; i<x; i++) {
				list.add(Integer.parseInt(st.nextToken()));
			}
			break;
		}
	}
}
