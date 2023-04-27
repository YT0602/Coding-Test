import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(bf.readLine());
		
		int[] arrA = new int[N];
		Integer[] arrB = new Integer[N];
		
		String[] arr = bf.readLine().split(" ");
		for (int i=0; i<N; i++) {
			arrA[i] = Integer.parseInt(arr[i]);
		}
		
		arr = bf.readLine().split(" ");
		for (int i=0; i<N; i++) {
			arrB[i] = Integer.parseInt(arr[i]);
		}
		// A는 오름차순, B는 내림차순정렬
		Arrays.sort(arrA);
		Arrays.sort(arrB, Collections.reverseOrder());
		
		int result = 0;
		for (int j=0; j<N; j++) {
			result += arrA[j]*arrB[j];
		}
		System.out.println(result);

		
	}
}
