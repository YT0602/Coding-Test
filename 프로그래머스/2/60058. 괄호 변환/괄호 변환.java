import java.util.*;

class Solution {
    public String solution(String p) {
        String answer = "";
        
        if (isCorrect(p)) return p;
        
        answer = transfer(p);
        return answer;
    }
    
    public String transfer(String w) {
        // 1. 빈문자열이면 반환
        if (w.isEmpty()) return "";
        // 2. 두 균형잡힌 문자열로 분리
        String u = devide(w);
        String v = w.substring(u.length());
        
        StringBuilder sb = new StringBuilder();
        
        // 3. 올바른 문자열이면
        if (isCorrect(u)) {
            // 1부터 재귀
            String x = transfer(v);
            // 결과 붙여서 반환
            sb.append(u).append(x);
            return sb.toString();
        // 4. 올바르지 않은 경우
        } else {
            // 4-1. 빈문자열에 ( 붙이기
            sb.append("(");
            // 4-2. v에 대해 1번부터 재귀
            String x = transfer(v);
            // 4-3. ) 붙이기
            sb.append(x).append(")");
            // 4-4. 앞뒤 제거하고 괄호 뒤집기
            u = u.substring(1, u.length()-1);
            for (int i=0; i<u.length();i++) {
                if (u.charAt(i) == '(') sb.append(")");
                else sb.append("(");
            }
            return sb.toString();
        }
        
    }
    
    public String isEmpty(String p) {
        if (p.isEmpty()) return "";
        else return p;
    }
    
    // 올바른 괄호 확인
    public boolean isCorrect(String p) {
        // 빈문자열
        if (p.isEmpty()) return true;
        
        Queue<String> q = new LinkedList<>();
        char[] arr = p.toCharArray();
        // 처음부터 불가능
        if (arr[0] == ')') return false;
        
        for (char c : arr) {
            // 여는괄호면 추가
            if (c == '(') q.add(String.valueOf(c));
            // 닫는괄호면 빼기
            else {
                String x = q.poll();
                // 빼야되는데 비어있는경우 실패
                if (x == null) return false;
            }
        }
        
        if (q.isEmpty()) return true; // 괄호가 모두 닫힌 경우 == 올바른 괄호
        else return false;
    }
    
    // 문자열 분리
    public String devide(String p) {
        char[] arr = p.toCharArray();
        StringBuilder sb = new StringBuilder();
        char first = arr[0];
        int cnt1 = 0;
        int cnt2 = 0;
        for (char c : arr) {
            if (c == first) {
                cnt1++;
                sb.append(c);
            } else {
                cnt2++;
                sb.append(c);
            }
            // 두 종류의 괄호 개수가 같아지면 균형잡힌 문자열이므로 return
            if (cnt1 == cnt2) {
                return sb.toString();
            }
        }
        return sb.toString();
    }
}