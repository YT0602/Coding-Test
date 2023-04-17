import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(bf.readLine());
		int cnt = 0;  // 그룹 단어 개수
		
		for (int i=0; i<N; i++) {
			String st = bf.readLine();
			boolean check[] = new boolean[26]; // 사용한 알파벳인지 체크
			boolean test = true; // 그룹단어인지 체크
			
			int l = st.length();
			// 첫 문자 사용 처리
			char tmp = st.charAt(0);
			int idx = st.charAt(0)-'a';
			check[idx] = true;
			for (int j=1;j<l;j++) {
				idx = st.charAt(j)-'a';
				// 앞의 문자와 다를 경우
				if (st.charAt(j) != tmp) {
					tmp = st.charAt(j);
					if (check[idx] == false) { // 사용하지 않은 문자라면
						check[idx] = true; // 사용처리 
					}else {
						test = false; // 사용했으면 그룹단어 아님
					}
				}
				
			}
			if (test) cnt++; // true 일때만 추가
		}
		System.out.println(cnt);
	}
}
