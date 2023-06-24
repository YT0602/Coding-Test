import java.io.*;
import java.util.*;
class Pos {
	int x;
	int y;
	Pos(int x, int y){
		this.x = x;
		this.y = y;
	}
}

public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int i=0; i<T; i++) {
			// 편의점 수
			int N = Integer.parseInt(bf.readLine());
			// 편의점 위치 배열
			ArrayList<Pos> arr = new ArrayList<>();
			StringTokenizer st = new  StringTokenizer(bf.readLine());
			// 출발점
			int home_X = Integer.parseInt(st.nextToken());
			int home_Y = Integer.parseInt(st.nextToken());
			// 편의점 좌표 추가
			for (int j=0; j<N; j++) {
				st = new StringTokenizer(bf.readLine());
				arr.add(new Pos(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
				
			}
			// 도착점
			st = new StringTokenizer(bf.readLine());
			int fes_X = Integer.parseInt(st.nextToken());
			int fes_Y = Integer.parseInt(st.nextToken());
			// BFS
			Queue<Pos> q = new LinkedList<>();
			q.add(new Pos(home_X, home_Y));
			
			boolean flag = false;
			while (!q.isEmpty()) {
				Pos cur = q.poll();
				// 현재위치에서 도착점까지 거리가 1000이하면 맥주 다 마시기전에 도착
				if (Math.abs(cur.x - fes_X)+Math.abs(cur.y-fes_Y) <= 1000) {
					flag = true;
					break;
				}
				// 현재위치에서 편의점까지 거리가 1000이하면
				// 맥주 다 마시기전에 편의점 들려서 충전
				for (int j=0; j<arr.size(); j++) {
					if (Math.abs(cur.x - arr.get(j).x)+Math.abs(cur.y-arr.get(j).y) <= 1000){
						// 현재 위치 업데이트
						q.add(new Pos(arr.get(j).x, arr.get(j).y));
						// 방문한 편의점 제거
						arr.remove(j);
					}
				}
			}
			// 페스티벌 도착
			if (flag) {
				System.out.println("happy");
			// 도착실패
			}else {
				System.out.println("sad");
			}
		}
		
	}

}