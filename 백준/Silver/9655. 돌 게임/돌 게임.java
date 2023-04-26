import java.io.*;
public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int num = Integer.parseInt(bf.readLine());
		
		if (num %2 == 1) {
			System.out.println("SK");
		}else {
			System.out.println("CY");
		}
	}
}
