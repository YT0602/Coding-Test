import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(bf.readLine());
		for (int i=0; i<N; i++) {
			String[] arr = bf.readLine().split(" ");
			int x1 = Integer.parseInt(arr[0]);
			int y1 = Integer.parseInt(arr[1]);
			int r1 = Integer.parseInt(arr[2]);
			int x2 = Integer.parseInt(arr[3]);
			int y2 = Integer.parseInt(arr[4]);
			int r2 = Integer.parseInt(arr[5]);
			
			System.out.println(turret(x1, y1, r1, x2, y2, r2));
		
	}
}
	public static int turret(int x1, int y1, int r1, int x2, int y2, int r2) {
		int circle_dis = (int)Math.pow(x2-x1, 2) + (int)Math.pow(y2-y1, 2);
		
		if (x1==x2 && y1 == y2 && r1==r2) {
			return -1;
		}
		else if (circle_dis > Math.pow(r1+r2, 2) || circle_dis < Math.pow(r2-r1,2)) {
			return 0;
		}
		else if (circle_dis == Math.pow(r1+r2, 2) || circle_dis == Math.pow(r2-r1, 2)) {
			return 1;
		}
		else {
			return 2;
		}
	}
}
