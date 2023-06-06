import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int minus = 0, zero = 0, one = 0;
	static int[][] arr;
	
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(bf.readLine());
		arr = new int[N][N];
		StringTokenizer st;
		
		for (int i=0; i < N; i++) {
			st = new StringTokenizer(bf.readLine(), " ");
			for (int j=0; j < N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		paper(0, 0, N);
		
		System.out.println(minus);
		System.out.println(zero);
		System.out.println(one);
	}
	
	public static void paper(int r, int c, int size) {
		if (samenum(r, c, size)) {
			if (arr[r][c] == -1) {
				minus++;
			}else if (arr[r][c] == 0) {
				zero++;
			}else {
				one++;
			}
			
		}else {
			int resize = size/3;
			for (int i=0; i<3; i++) {
				for (int j=0; j<3; j++) {
					paper(r+resize*i, c + resize*j, resize);
				}
			}
			
		}
	}
	// 사작형 안이 모두 같은 숫자인지 체크
	public static boolean samenum(int r, int c, int size) {
		if (size == 1) {
			return true;
		} else {
			int first = arr[r][c];
			
			for (int i = r; i < r+size; i ++) {
				for (int j = c; j < c+size; j++) {
					if (arr[i][j] != first) {
						return false;
					}
				}
			}
			return true;
		}
	}

}