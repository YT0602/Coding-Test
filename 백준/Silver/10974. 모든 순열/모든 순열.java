import java.util.*;
import java.io.*;


public class Main {
	static int N;
	static boolean[] visit;
	static int[] arr, output;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		
		visit = new boolean[N+1];
		arr = new int[N];
		output = new int[N];
		
		for (int i=0; i<N; i++) {
			arr[i] = i+1;
		}
	
		comb(arr, 0);
		
	}
	
	public static void comb(int[] arr, int cnt) {
		if (cnt == N) {
			for (int i=0; i<N; i++) {
				System.out.print(output[i] + " ");
			}
			System.out.println();
			return;
		}
		
		for (int i=0; i<N; i++) {
			if(!visit[i]) {
				output[cnt] = arr[i]; 
				visit[i] = true;
				comb(arr, cnt+1);
				visit[i] = false;
			}
		}
	}

}
