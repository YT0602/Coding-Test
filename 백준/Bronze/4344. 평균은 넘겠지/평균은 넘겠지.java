import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int tc = Integer.parseInt(bf.readLine());
		int[] arr; // 성적리스트
		StringTokenizer st;
		
		for (int i=0;i<tc;i++) {
			st = new StringTokenizer(bf.readLine(), " "); // 공백기준으로 분리
			
			int N = Integer.parseInt(st.nextToken()); // 맨 앞은 학생 수
			arr = new int[N]; // 나머지는 성적
			
			double sum = 0; // 성적 합
			
			for (int j=0;j<N;j++) {
				int val = Integer.parseInt(st.nextToken()); // 성적 저장
				arr[j] = val;
				sum += val;
			}
			
			double mean = (sum/N); // 평균
			double cnt = 0;
			
			//평균 넘는 학생
			for (int j=0;j<N;j++) {
				if (arr[j] > mean) {
					cnt++;
				}
			}
			
			System.out.printf("%.3f%%\n", (cnt/N)*100);
			
			}
}
}
