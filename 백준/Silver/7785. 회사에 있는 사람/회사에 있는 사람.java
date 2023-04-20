import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(bf.readLine());
		HashSet<String> set = new HashSet<>();
		
		for (int i=0; i<N; i++) {
			String[] input = bf.readLine().split(" ");
			String name = input[0];
			String log = input[1];
			
			if (log.equals("enter")) {
				set.add(name);
			}else if (log.equals("leave")) {
				set.remove(name);
			}
			
		}
		List<String> list = new ArrayList(set);
		Collections.sort(list, Collections.reverseOrder());
		
		for (int i=0; i<list.size();i++) {
		System.out.println(list.get(i));
		
		}
	}
}
