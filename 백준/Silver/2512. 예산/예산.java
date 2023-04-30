import java.util.*;
import java.io.*;
public class Main {
	static int N;
	static int cost;
	static int request;
	static int[] arr;
	
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		// 개수
		N = Integer.parseInt(bf.readLine());
		arr = new int[N];
        // 요청예산 배열
		StringTokenizer st = new StringTokenizer(bf.readLine());
		for (int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			request += arr[i];
		}
        // 최대예산
		cost = Integer.parseInt(bf.readLine());

		Arrays.sort(arr);
		System.out.println(binary());
	}
	// 이분탐색
	static int binary() {
        // 최대 예산보다 합이 적으면 요청 중 최대값 반환
		if (request <= cost) {
			return arr[N-1];
		}
		int start = 0;
		int end = cost;
		
		while (start<=end) {
			int cur = 0;
			int mid = (start+end)/2; // 상한가
			
			for (int i=0; i<N; i++) {
				if(arr[i]>mid) {
					cur += mid;
				}else {
					cur += arr[i];
				}
			}
			// 예산 모자란 경우 상한가 낮춤
			if (cur > cost) {
				end = mid-1;
			}
			// 예산 남는 경우 상한가 높임
			else if(cur<cost) {
				start = mid+1;
			}
			else return mid;
		}
		return end;
	}
}