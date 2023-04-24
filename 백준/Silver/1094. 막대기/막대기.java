import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] arr = new int [7];
		int x = sc.nextInt();
		
		int i = 0;
		while (x>0) {
			arr[i] = x%2;
			x /= 2;
			i++;
		}
		int cnt = 0;
		for (int j=0; j<7; j++) {
			if (arr[j]==1) {
				cnt++;
			}
		}
		System.out.println(cnt);
	}

}
