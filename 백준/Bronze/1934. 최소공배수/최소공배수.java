import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
        
		StringBuilder sb = new StringBuilder();
 
		for(int i = 0; i < N; i++) {
			
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			int D = gcd(a, b);	// 최소공배수
			
			sb.append(a * b / D).append('\n');
		}
		System.out.println(sb);
		
	}
	public static int gcd(int a, int b) {
 
		while (b != 0) {
			int x = a % b; // 나머지
 
			// GCD(a, b) = GCD(b, x)
			a = b;
			b = x;
		}
		return a;
	}
}