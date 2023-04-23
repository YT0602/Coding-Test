import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		int top = 1;
		int bot = 1;
		int num = 1;
		int line = 1;
		while (num<x) {
			line++;
			// 라인의 끝 번호
			num = line*(line+1)/2;
			}
		// 라인에서 몇번째인지
		int cnt = x-(line-1)*line/2;
		if (line%2==0) {
			top = cnt;
			bot = line-cnt+1;
		}
		else {
			top = line-cnt+1;
			bot = cnt;
		}
		System.out.println(top + "/" + bot);
		
	}
}
