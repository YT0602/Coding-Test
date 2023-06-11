import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(bf.readLine());
		StringTokenizer st = new StringTokenizer(bf.readLine());
		int[] arr = new int[N+1];
		List<Integer> ans = new ArrayList<>();
		
		for (int i=1; i<N+1; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			
		}
		for (int i=N; i>=1; i--) {
			ans.add(arr[i], i);
		}
		for (int x:ans) {
			System.out.print(x+" ");
		}
		
	}

}
