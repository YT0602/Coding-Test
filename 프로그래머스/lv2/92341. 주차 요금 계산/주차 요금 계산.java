import java.util.*;
import java.io.*;

class Solution {
    static Map<String, Integer> carRecord = new HashMap<>(); // 차 출입기록
    static Map<Integer, Integer> carFee = new HashMap<>(); // 주차 요금
    public int[] solution(int[] fees, String[] records) {

        // 주차된 차
        Map<String, String> parking = new HashMap<>();
        
        for (int i=0; i < records.length; i++){
            String[] record = records[i].split(" ");
            // 입차
            if (record[2].equals("IN")){
                parking.put(record[1], record[0]);
            } else { // 출차면 시간 계산
                // 입차시간, 출차시간, 차 번호
                times(parking.get(record[1]), record[0], record[1]);
                // 주차 목록에서 제거
                parking.remove(record[1]);
            }
        }
        // 남아있는 주차 차량 있으면 23:59 출차로 시간 계산
        if (!parking.isEmpty()){
            for (String num : parking.keySet()){
                times(parking.get(num), "23:59", num);
            }
        }
        // 요금계산
        calcul(fees);
        
        // 차 번호 오름차순 정렬
        List<Map.Entry<String, Integer>> list = new ArrayList<>(carRecord.entrySet());
        list.sort(Map.Entry.comparingByKey());
        
        // 최종 요금
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i).getValue();
        }
        
        return answer;
    }
    public void times(String inTime, String outTime, String carNum){
        // 주차 시간을 분으로 계산
        String[] outTemp = outTime.split(":");
        int outMin = Integer.parseInt(outTemp[0]) * 60 + Integer.parseInt(outTemp[1]);
        String[] inTemp = inTime.split(":");
        int inMin = Integer.parseInt(inTemp[0]) * 60 + Integer.parseInt(inTemp[1]);
        // 총 주차시간
        int parkingTime = outMin - inMin;
        // 주차시간 업데이트
        carRecord.put(carNum, carRecord.getOrDefault(carNum, 0) + parkingTime);
    }
    public void calcul(int[] fees){
        for (String car : carRecord.keySet()){
            // 기본시간보다 작을때
            if (carRecord.get(car) < fees[0]){
                carRecord.put(car, fees[1]);
            } else{
                // 추가 시간
                double addTime = carRecord.get(car) - fees[0];
                // 추가 요금
                double addFee = Math.ceil(addTime/fees[2]) * fees[3];
                // 총 요금
                int totalFee = fees[1] + (int)addFee;
                carRecord.put(car, totalFee);
            }
        }
    }
}