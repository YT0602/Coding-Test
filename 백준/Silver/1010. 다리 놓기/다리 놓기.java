import java.util.*;

public class Main {
	 static int[][] dp = new int[31][31];
	
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();

        for (int i = 0; i < tc; i++) {
            int west = sc.nextInt();
            int east = sc.nextInt();
            // 동쪽개수중에 서쪽개수 선택하는 조합
            System.out.println(combi(east, west));
        }
    }
    // 조합
    public static int combi(int n, int r) {
    	
        if (dp[n][r] > 0) {
            return dp[n][r];
        } else if (n == r || r == 0) {
            return dp[n][r] = 1;
        } else {
            return dp[n][r] = combi(n - 1, r - 1) + combi(n - 1, r);
        }
    }
}
