import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static int[][] arr; //  2차원 배열
	static StringBuilder sb = new StringBuilder(); // 출력 문자열을 저장

	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(bf.readLine());
		arr = new int[N][N]; // 2차원 배열 초기화
		
		// 2차원 배열
		for (int i=0; i<N; i++) {
			String line = bf.readLine();
			for (int j=0; j<N; j++) {
				// 문자를 숫자로 변환하므로 아스키 코드값으로 계산
				arr[i][j] = line.charAt(j) - '0';
			}	
		}

		Tree(0, 0, N);

		System.out.println(sb);
		
	}

	// 쿼드트리를 생성하는 재귀 함수
	public static void Tree(int row, int col, int size) {
		// 현재 부분 트리의 모든 요소가 같은 값인 경우
		if (check(row, col, size)) {
			sb.append(arr[row][col]); // 그 값을 StringBuilder에 추가
		}
		else { // 그렇지 않은 경우
			int half = size/2; // 현재 부분 트리를 4개의 부분 트리로 나눔
			sb.append("("); // 여는 괄호를 추가
			// 4개의 부분 트리에 대해 재귀 호출
			Tree(row, col, half);
			Tree(row, col+half, half);
			Tree(row+half, col, half);
			Tree(row+half, col+half, half);
			sb.append(")"); // 닫는 괄호를 추가
		}
	}

	// 현재 부분 트리의 모든 요소가 같은 값인지 확인하는 함수
	public static boolean check(int r, int c, int size) {
		int num = arr[r][c]; // 첫 번째 요소의 값을 저장
		
		// 모든 요소에 대해
		for (int i=r; i<r+size; i++) {
			for (int j=c; j<c+size; j++) {
				// 현재 요소의 값이 첫 번째 요소의 값과 다른 경우 false 반환
				if (arr[i][j] != num) {
					return false;
				}
			}
		}

		// 모든 요소의 값이 같은 경우 true 반환
		return true;
	}
}