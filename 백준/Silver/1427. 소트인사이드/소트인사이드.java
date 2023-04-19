import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws IOException {
		
		// 수학 계산, 카운팅정렬
//		Scanner sc = new Scanner(System.in);
//		int[] counting = new int[10];
//		int N = sc.nextInt();
		// 뒷자리부터 하나씩 배열에 저장
//		while (N!=0) {
//			counting[N%10]++;
//			N /= 10;
//			
//		}
//		
//		for (int i=9; i>=0; i--) {
//			// 카운트 1씩 줄이면서 출력
//			while (counting[i]--> 0) {
//				System.out.print(i);
//			}
//		}
        
		// sort 사용
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
//		char[] arr = sc.nextLine().toCharArray();
		char[] arr = bf.readLine().toCharArray();
		
		Arrays.sort(arr);
		
		for (int i=arr.length-1; i>=0;i--) {
			System.out.print(arr[i]);
		}
	}
}
