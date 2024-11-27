import java.util.*;
import java.util.regex.Pattern;

class Solution {
    static HashSet<HashSet<String>> result;
    static List<List<String>> idCase;
    static int answer;
    public int solution(String[] user_id, String[] banned_id) {
        
        idCase = new ArrayList<>();
        result = new HashSet<>();
        
        for (String ban : banned_id) {
            idCase.add(matchingId(ban, user_id));
        }
        
        find(0, new HashSet<>());
        
        return result.size();
    }
    
    // 각 제재아이디별 가능한 사용자 아이디 찾기
    public List<String> matchingId(String ban, String[] user_id) {
        // * 치환
        String regex = ban.replace("*", ".");
        
        List<String> match = new ArrayList<>();
        // 정규표현식에 매치되는 id 추가
        for (String user : user_id) {
            // 길이 다르면 생략
            if (user.length() != ban.length()) continue;
            
            if(Pattern.matches(regex, user)) {
                match.add(user);        
            }
        }
        return match;
    }
    
    // 경우의 수 찾기
    public void find(int depth, HashSet<String> set) {
        // 조합 끝나면 경우의 수 추가
        if (depth == idCase.size()) {
            result.add(new HashSet<>(set)); // 동일 조합 방지
            return;
        }
        // 해당 banned id 의 조합 가능 id list
        List<String> list = idCase.get(depth);
        
        for (String id : list) {
            // 없으면 추가하고 다음 case
            if(!set.contains(id)) {
                set.add(id);
                find(depth+1, set);
                set.remove(id);
            }
        }
    }
    
}