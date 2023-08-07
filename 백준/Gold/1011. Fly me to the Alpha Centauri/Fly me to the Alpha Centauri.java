import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());

		for (int t = 0; t < T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());

			int dis = y - x; // 이동할 거리
			int ans = 0; // 이동 횟수

			int max = (int) Math.sqrt(dis);

			if (max == Math.sqrt(dis)) {
				ans = max * 2 - 1;
			} else if (dis <= max * max + max) {
				ans = max * 2;
			} else {
				ans = max * 2 + 1;
			}
			
			bw.write(ans + "\n");

		}
		bw.flush();
		bw.close();
	}

}