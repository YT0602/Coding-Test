import java.util.*;

class Solution {
    static List<Set<Integer>> keys = new ArrayList<>();
    static int answer = 0;
    public int solution(String[][] relation) {
        
        int col = relation[0].length;
        
        // 크기별 조합 구하기
        for (int i=1; i<=col; i++) {
            combination(0, col, i, new HashSet<>(), relation);
        }
        return answer;
    }
    // 조합
    public void combination(int idx, int col, int size, Set<Integer> set, String[][] relation) {
        // 특정 크기의 조합 완성되면
        if (set.size() == size) {
            // 유일성 검사
            if (checkUnique(set, relation)) {
                // 최소성 검사
                for (Set<Integer> key : keys) {
                    if (set.containsAll(key)) {
                        return;
                    }
                }
                keys.add(set);
                answer++;
                return;
            }
            return;
        }
        
        for (int i=idx; i<col; i++) {
            Set<Integer> newSet = new HashSet<>(set);
            newSet.add(i);
            combination(i+1, col, size, newSet, relation);
        }
    }
    // 유일성 검사
    public boolean checkUnique(Set<Integer> set, String[][] relation) {
        List<String> list = new ArrayList<>();
        // 각 튜플 돌면서
        for (String[] tuple : relation) {
            StringBuilder sb = new StringBuilder();
            // 후보키 조합 생성
            for (Integer idx : set) {
                sb.append(tuple[idx]);
            }
            // 중복 확인
            if (!list.contains(sb.toString())) {
                list.add(sb.toString());
            } else {
                return false;
            }
        }
        return true;
    }
}