import java.io.*;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[] arr;
	static int[] plus, minus;
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(bf.readLine());
		
		arr = new int[N];
		plus = new int[N]; // 증가하는 수열
		minus = new int[N]; // 감소하는 수열
		
		StringTokenizer st = new StringTokenizer(bf.readLine());
		for (int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		LIS();
		LDS();
		
		int ans = 0;
		for (int i=0; i<N; i++) {
			if (ans < plus[i] + minus[i]) {
				ans = plus[i] + minus[i];
			}
		}
		System.out.println(ans-1); // 중복 제거
		
	}
	// 가장 긴 증가하는 부분 수열 계산
	public static void LIS() {
		for (int i=0; i<N; i++) {
			plus[i] = 1;
			for (int j=0; j<i; j++) {
				if (arr[j] < arr[i] && plus[i] < plus[j] + 1) {
					plus[i] = plus[j] + 1;
				}
			}
		}
	}
	// 가장 긴 감소하는 부분 수열 계산
	public static void LDS() {
		for (int i=N-1; i>=0; i--) {
			minus[i] = 1;
			for (int j=N-1; j>i; j--) {
				if (arr[j] < arr[i] && minus[i] < minus[j] + 1) {
					minus[i] = minus[j] + 1;
				}
			}
		}
	}

}
