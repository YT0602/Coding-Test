import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = s.length();
        
        String tmp;
        int cnt;
        for (int i=1; i<=s.length()/2; i++) {
            StringBuilder sb = new StringBuilder();
            tmp = "";
            cnt = 1;
            for (int j=0; j<=s.length()-i; j+=i) {
                String sub = s.substring(j,j+i); // 문자열 i개만큼 자르기
                if (!tmp.equals(sub)) { // 문자열 다른경우
                    if (cnt == 1) { // 반복없는경우 문자만
                        sb.append(tmp);
                    } else {
                        // 반복횟수+문자
                        sb.append(cnt);
                        sb.append(tmp);
                        cnt = 1;
                    }
                    tmp = sub;
                } else { // 같은 문자일때
                    // 개수 올리고 넘어가기
                    cnt++;
                    continue;
                }
            }
            // 나머지 추가
            if (cnt > 1) {
                sb.append(cnt);
                sb.append(tmp);
            } else {
                sb.append(tmp);
            }
            
            // 길이가 나누어떨어지지 않으면 나머지 추가
            if (s.length() % i != 0) {
                int x = s.length()%i;
                sb.append(s.substring(s.length()-x));
            }
            answer = Math.min(answer, sb.length());
        }
        
        return answer;
    }
}