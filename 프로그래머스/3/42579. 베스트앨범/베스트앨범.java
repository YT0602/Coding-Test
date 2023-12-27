import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        Map<String, Integer> album = new HashMap<>();
        Map<String, Map<Integer, Integer>> genreAlbum = new HashMap<>();
        // 장르별 맵 초기화
        for (String genre:genres) {
            genreAlbum.put(genre, new HashMap<>());
        }
        
        for (int i=0; i<genres.length; i++) {
            // 재생횟수 카운트
            int cnt = album.getOrDefault(genres[i], 0);
            album.put(genres[i], cnt+plays[i]);
            // 장르별 정리
            genreAlbum.get(genres[i]).put(i, plays[i]);
        }
        // 재생횟수 기준 장르 정렬
        List<String> sortedGenres = new ArrayList(album.keySet());
        Collections.sort(sortedGenres, (s1, s2) -> album.get(s2) - album.get(s1));
        
        for (String genre : sortedGenres) {
            // 장르별 앨범 재생횟수 기준 정렬
            Map<Integer, Integer> map = genreAlbum.get(genre);
            List<Integer> sortedPlay = new ArrayList(map.keySet());
            Collections.sort(sortedPlay, (s1, s2) -> map.get(s2) - map.get(s1));
            // 최대 두개 추가
            answer.add(sortedPlay.get(0));
            if (sortedPlay.size() > 1) answer.add(sortedPlay.get(1));
        }
        
        return answer.stream().mapToInt(i -> i).toArray(); // 리스트를 배열로 변환
    }
}