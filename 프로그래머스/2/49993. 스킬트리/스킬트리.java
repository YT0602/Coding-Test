import java.util.*;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        
        for (int i=0; i<skill_trees.length; i++) {
            // 정규표현식으로 스킬트리 포함 안되는 스킬 제거
            skill_trees[i] = skill_trees[i].replaceAll("[^"+skill+"]", "");
            
            boolean flag = true;
            for (int j=0; j<skill.length(); j++) {
                // 스킬 비교
                if (j<skill_trees[i].length() && skill.charAt(j) != (skill_trees[i].charAt(j))) {
                    flag = false;
                }
            }
            if (flag) answer++;
        
        }
        
        return answer;
    }

}