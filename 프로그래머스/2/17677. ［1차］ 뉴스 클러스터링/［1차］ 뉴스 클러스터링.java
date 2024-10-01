import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        
        List<String> list1 = devide(str1.toLowerCase());
        List<String> list2 = devide(str2.toLowerCase());
        // 둘 다 공집합인 경우
        if (list1.size() == 0 && list2.size() == 0) return 65536;
        
        List<String> inter = new ArrayList<>(); // 교집합
        List<String> union = new ArrayList<>(); // 합집합
        
        // 정렬
        Collections.sort(list1);
        Collections.sort(list2);
        
        for (String st : list1) {
            // 교집합 추가
            if (list2.remove(st)) {
                inter.add(st);
            }
            // 합집합 추가
            union.add(st);
        }
        // 남은 문자 합집합 추가
        for (String st:list2) {
            union.add(st);
        }
        // 유사도 계산
        double jk = (double) inter.size() / (double)union.size();
        return (int)(jk*65536);
    }
   
    
    // 다중집합 만들기
    public List<String> devide(String str) {
        List<String> list = new ArrayList<>();
        
        for (int i=0; i<str.length()-1; i++) {
            char a = str.charAt(i);
            char b = str.charAt(i+1);
            // 영문자 확인
            if (Character.isLetter(a) && Character.isLetter(b)) {
                StringBuilder sb = new StringBuilder();
                sb.append(a).append(b);
                list.add(sb.toString());
            }
        }
        return list;
    }
}