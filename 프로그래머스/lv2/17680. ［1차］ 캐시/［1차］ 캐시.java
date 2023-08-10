import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        
        LinkedList<String> cache = new LinkedList<>();
        int answer = 0; // 실행시간
        // 캐시 크기 0인 경우
        if (cacheSize == 0) {
            answer = cities.length * 5;
            return answer;
        }
        for (String city : cities){
            city = city.toLowerCase(); // 대소문자 구분 x
            if (cache.contains(city)) { // 캐싱된 경우
                cache.remove(city);
                cache.add(city); // 제거하고 맨뒤에 추가
                answer += 1; // 캐시 히트
            } else {
                if (cache.size() == cacheSize) {
                    cache.poll(); // 꽉 차면 가장 오래된거 제거
                }
                cache.add(city);
                answer += 5; // 캐시 미스
            }
        }
        
        return answer;
    }
}