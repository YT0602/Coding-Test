import java.io.*;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		int H = Integer.parseInt(st.nextToken());
		int W = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[W]; // 블록 높이 배열
		int[] rain = new int[W]; // 빗물 높이 배열
		
		int height = 0;
		st = new StringTokenizer(bf.readLine());
		for (int i=0; i<W; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			height = Math.max(height, arr[i]);
			rain[i] = height; // 오른쪽으로 가면서 최대 높이 저장
		}
		
		height = 0;
		int ans = 0;
		for (int i=W-1; i>=0; i--) { // 다시 왼쪽으로 가면서
			height = Math.max(height, arr[i]); // 블록 최대 높이
			rain[i] = Math.min(height,  rain[i]); // 빗물 채워질 수 있는 높이
			ans += rain[i] - arr[i]; // 빗물 높이 - 블록높이
		}
		System.out.println(ans);
	
	}
}