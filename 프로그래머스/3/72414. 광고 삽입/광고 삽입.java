import java.util.*;

class Solution {
    public String solution(String play_time, String adv_time, String[] logs) {
        int play = convertTime(play_time);
        int adv = convertTime(adv_time);
        
        int[] video = new int[play+1];
        // 누적합으로 구간별 시청자 표시
        for (String log : logs) {
            String startTime = log.split("-")[0];
            String endTime = log.split("-")[1];
            int start = convertTime(startTime);
            int end = convertTime(endTime);
            for (int i=start; i<end; i++) {
                video[i]++;
            }
        }
        // 슬라이딩 윈도우
        int adStart = 0;
        long sum = 0;
        long max = 0;
        // 젤 첫 부분
        for (int i=0; i<adv; i++) {
            sum += video[i];
        }
        max = sum;
        // 이후부터 슬라이딩
        for (int i=adv; i<play; i++) {
            sum += video[i];
            sum -= video[i-adv];
            // 최대값 갱신 시 광고 첫 시작 시간도 갱신
            if (max < sum) {
                max = sum;
                adStart = i-adv+1;
            }
        }
        // int 다시 시간 형식으로 변환
        String answer = String.format("%02d:%02d:%02d", adStart / 3600, (adStart % 3600) / 60, adStart % 60);

        return answer;
    }
    // 시간을 int형으로 변환
    public int convertTime(String time) {
        int intTime = 0;
        String[] times = time.split(":");
        int hour = Integer.parseInt(times[0]);
        int min = Integer.parseInt(times[1]);
        int sec = Integer.parseInt(times[2]);
        
        intTime += hour*60*60;
        intTime += min*60;
        intTime += sec;
        
        return intTime;
    }
}