import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int N = Integer.parseInt(br.readLine());
		long[] arr = new long[N]; // 용액 특성값 배열

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		// 오름차순 정렬
		Arrays.sort(arr);
		long[] ans = new long[3]; // 세 용액 배열

		long mn = Long.MAX_VALUE;
		// 용액 하나를 한번씩 순회하면서 나머지 두 용액을 투 포인터로 찾기
		for (int i = 0; i < N - 2; i++) { 
			int start = i;
			int mid = i + 1;
			int end = N - 1;

			while (mid < end) {
				// 농도 합
				long sum = arr[start] + arr[mid] + arr[end];
				long abs_sum = Math.abs(sum);
				// 최소값 갱신
				if (mn > abs_sum) {
					mn = abs_sum;
					ans[0] = arr[start];
					ans[1] = arr[mid];
					ans[2] = arr[end];

				}
				// 0이면 다 작아질 수 없으므로 중단
				if (abs_sum == 0) {
					break;
				// 최소값보다 크고 양수이면 end를 뒤로 한칸 이동
				} else if (sum > 0) {
					end--;
				// 최소값보다 크고 음수이면 mid를 앞으로 한칸 이동
				} else {
					mid++;
				}
			}
		}
		bw.write(ans[0] + " " + ans[1] + " " + ans[2] + "\n");
		bw.flush();
		bw.close();
	}
}
