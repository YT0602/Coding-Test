
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		char[][] arr = new char[5][15];
		
		
		for (int i=0; i<5; i++) {
			String st = bf.readLine();
			// 배열에 한글자씩 입력
			for (int j=0; j<st.length(); j++) {
				arr[i][j] = st.charAt(j);
			}
		}
		
		//한글자씩 출력
		for (int i=0; i < 15; i++) {
			for (int j=0; j<5; j++) {
				if (arr[j][i] == '\0') continue;
				System.out.print(arr[j][i]);
			}
		}
	}
}
