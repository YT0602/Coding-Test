import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int[] arr = new int [N];
		for (int i=0; i<N; i++) {
			int rope = sc.nextInt();
			arr[i] = rope;
		}
		Arrays.sort(arr);
		int len = arr.length;
		int mx = 0;
		for (int j=0; j<arr.length; j++) {
			if (mx < arr[j]*len) {
				mx = arr[j]*len;
			}
			len--;
		}
		System.out.println(mx);
		
	}
}