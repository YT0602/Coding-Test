
import java.io.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String st = bf.readLine();
		int l = st.length();
		int ans = 1;
		for (int i=0;i<=st.length()/2;i++) {
			l--;
			if (st.charAt(i)!=st.charAt(l)) {
				ans = 0;
			}
		}
		System.out.print(ans);
			
		}
	}