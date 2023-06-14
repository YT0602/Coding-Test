import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static int[][] graph;
	
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(bf.readLine());
		graph = new int [N][N];
		
		// 간선 연결
		for (int i=0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			for (int j=0; j<N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		// 플로이드 워셜
		for (int l=0; l<N; l++) {
			for (int i=0; i<N; i++) {
				for (int j=0; j<N; j++) {
					// i에서 l을 거쳐 j로 가는 경로가 존재한다면(i->l->j), 경로를 1로 표시
					if (graph[i][l]==1 && graph[l][j] == 1) {
						graph[i][j] = 1;
					}
				}
			}
		}
		for (int i=0; i<N; i++) {
			// 각 줄마다 출력
			StringBuilder sb = new StringBuilder();
			for (int j=0; j<N; j++) {
				if (j == N-1) {
					sb.append(graph[i][j]);
				}else {					
					sb.append(graph[i][j] + " ");
				}
			}
			System.out.println(sb);
		}
	}
}