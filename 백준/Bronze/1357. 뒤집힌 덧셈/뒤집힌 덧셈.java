import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int X = Integer.parseInt(st.nextToken());
		int Y = Integer.parseInt(st.nextToken());
		
		int ans = Rev(Rev(X) + Rev(Y));
		
		bw.write(ans+"\n");
		bw.flush();
		bw.close();
	}

	public static int Rev(int N) {
		String str = "";
		while (N>0) {
			str += N % 10;
			N /= 10;
		}
		return Integer.parseInt(str);
	}
}
