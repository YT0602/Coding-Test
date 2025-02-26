import java.util.*;

class Solution {
    public int solution(int[][] points, int[][] routes) {
        int answer = 0;
        // 로봇별 이동 좌표 기록 리스트
        List<List<int[]>> robots = new ArrayList<>();
        
        for (int[] route : routes) {
            // 각 로봇의 이동 좌표 기록 리스트
            List<int[]> location = new ArrayList<>();
            location.add(points[route[0]-1]); // 시작위치 추가
            for (int i=0; i<route.length-1; i++) {
                // 시작 위치
                int[] start = points[route[i]-1];
                // 다음 목표 위치
                int[] target = points[route[i+1]-1];
                // 경로 추가
                location.addAll(move(start, target));
            }
            robots.add(location);
        }
        // 가장 많이 이동한 횟수 찾기
        int maxMove = 0;
        for (int i=0; i<robots.size(); i++) {
            List<int[]> location = robots.get(i);
            maxMove = Math.max(location.size(), maxMove);
        }
        
        // 같은 시간에 같은 위치인 경우 카운트
        for (int i=0; i<maxMove; i++) {
            Map<String, Integer> map = new HashMap<>(); // 위치별 로봇 수 map
            for (List<int[]> location : robots) {
                if (location.size() <= i) continue; // 이동 끝났으면 건너뜀
                
                int[] cur = location.get(i);
                String curString = Arrays.toString(cur); // 일치 확인하기위해 string으로 변경
                
                if (!map.containsKey(curString)) {
                    map.put(curString, 1);
                } else if (map.get(curString) == 1) { // 해당 위치에 이미 로봇있으면 충돌 추가하고 로봇 수도 추가
                    map.put(curString, map.get(curString)+1);
                    answer++;
                }
            }
        }
        return answer;
    }
    // 이동 좌표 기록
    public List<int[]> move(int[] start, int[] target) {
        List<int[]> location = new ArrayList<>();
        
        int[] cur = start;
        int r = cur[0];
        int c = cur[1];
        // r 방향부터 같은 행까지 이동하면서 위치 기록
        if (start[0] < target[0]) {
            while (r < target[0]) {
                r++;
                location.add(new int[]{r, cur[1]});
            }
        } else if (start[0] > target[0]) {
            while (r > target[0]) {
                r--;
                location.add(new int[]{r, cur[1]});
            }
        }
        // 같은 열까지 이동하면서 위치 기록
        if (start[1] < target[1]) {
            while (c < target[1]) {
                c++;
                location.add(new int[]{r, c});
            }
        } else if (start[1] > target[1]) {
            while (c > target[1]) {
                c--;
                location.add(new int[]{r, c});
            }
        }
        return location;
        
    }
}