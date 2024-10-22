import java.util.*;

class Solution {
    static boolean[] visited;
    static long answer = 0;
    public long solution(String expression) {
        
        Set<String> operator = new HashSet<>();
        // 연산자만 남겨서 set에 추가
        String opString = expression.replaceAll("[0-9]","");
        for (char c : opString.toCharArray()) {
            operator.add(c+"");
        }
        visited = new boolean[operator.size()];
        
        combination(new ArrayList(operator), new ArrayList<>(), expression);
        
        return answer;
    }
    // 연산자 조합하기
    public void combination(List<String> operator, List<String> result, String expression) {
        // 조합 완성되면 계산
        if (result.size() == operator.size()) {
            long num = devide(result, 0, expression);
            // 음수면 부호 바꾸기
            if (num < 0) num = -num;
            // 최댓값 갱신
            answer = Math.max(answer, num);
            return;
        }
        // DFS
        for (int i=0; i<operator.size(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                result.add(operator.get(i));
                combination(operator, result, expression);
                visited[i] = false;
                result.remove(result.size()-1);
            }
        }
    }
    
    public long devide(List<String> operator, int depth, String expression) {
        // 숫자만 남은경우
        if (expression.replaceAll("[0-9]", "").equals("")) return Long.parseLong(expression);
        // 해당 순위 연산자 없으면 다음순위로 진행
        if (!expression.contains(operator.get(depth))) {
            return devide(operator, depth+1, expression);
        }
        // 연산자 기준으로 split
        String[] exArr;
        if (operator.get(depth).equals("-")) {
            exArr = expression.split(operator.get(depth));
        } else {
            exArr = expression.split("\\"+operator.get(depth));   
        }
        List<Long> numbers = new ArrayList<>();
        for (String ex : exArr) {
            // 재귀호출
            long num = devide(operator, depth+1, ex);
            numbers.add(num);
        }
        // 숫자 순서대로 계산
        long num1 = numbers.get(0);
        for (int i=1; i<numbers.size(); i++) {
            num1 = calcul(num1, numbers.get(i), operator.get(depth));
        }
        return num1;
        
    }
    // 계산
    public long calcul(long num1, long num2, String op) {
        if (op.equals("+")) return num1+num2;
        else if (op.equals("-")) return num1-num2;
        else return num1*num2;
    }
}