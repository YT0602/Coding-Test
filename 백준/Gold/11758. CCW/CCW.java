import java.io.*;
import java.util.*;
class Point {
	int x, y;
	// 점 좌표
	Point(int x, int y){
		this.x = x;
		this.y = y;
	}
}

public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st;
		
		Point[] p = new Point[3];
		
		for (int i=0; i<3; i++) {
			// x, y좌표 받아서 포인트 생성
			st = new StringTokenizer(bf.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			
			p[i] = new Point(x, y);
		}
		System.out.println(CCW(p));
		
	}
	
	public static int CCW(Point[] p) {
		// CCW 공식
		int prod1 = (p[0].x * p[1].y) + (p[1].x * p[2].y) + (p[2].x * p[0].y);
		int prod2 = (p[0].y * p[1].x) + (p[1].y * p[2].x) + (p[2].y * p[0].x);
		
		// 0보다 작으면 시계방향, 크면 반시계, 0이면 일직선
		if ((prod1 - prod2) < 0) {
			return -1;
		} else if ((prod1 - prod2) == 0) {
			return 0;
		}else {
			return 1;
		}
	}

}