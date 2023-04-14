import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] arr = new int[N];
		
		for (int i=0;i<N; i++) {
			arr[i] = i+1;
		}

		for (int i=0;i<M;i++) {
			int a = sc.nextInt()-1;
			int b = sc.nextInt()-1;
			
			if (a < b) {

				for (int j=a;j<b+1;j++) {
					int tmp = arr[j];
					arr[j] = arr[b];
					arr[b] = tmp;
					b--;
					
			}
		}
		}
		for (int j=0;j<N;j++) {
			System.out.print(arr[j]+" ");
		}
	}
}