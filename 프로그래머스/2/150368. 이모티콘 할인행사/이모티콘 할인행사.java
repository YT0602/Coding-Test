import java.util.*;

class Solution {
    int[] percent = new int[]{40, 30, 20, 10};
    int member = 0;
    int sell = 0;
    public int[] solution(int[][] users, int[] emoticons) {
        int[] answer = {0, 0};
        
        int[] salePercent = new int[emoticons.length];
        
        combination(salePercent, 0, users, emoticons);
        
        answer[0] = member;
        answer[1] = sell;
        
        return answer;
    }
    // 할인율 조합 만들기
    public void combination(int[] salePercent, int idx, int[][] users, int[] emoticons) {
        if (idx == emoticons.length) { // 조합 완성되면 계산
            calcul(salePercent, users, emoticons);
            return;
        }
        for (int i=0; i<4; i++) {
            salePercent[idx] = percent[i];
            combination(salePercent, idx+1, users, emoticons);
        }
    }
    // 할인율 토대로 멤버, 판매액 계산
    public void calcul(int[] salePercent, int[][] users, int[] emoticons) {
        int tmpMember = 0;
        int tmpSell = 0;
        for (int[] user : users) {
            int targetPercent = user[0]; // 구매기준 할인율
            int targetPrice = user[1]; // 최대 구매 금액
            
            int total = 0; // 현재 사용자의 총 구매 금액
            for (int i=0; i<emoticons.length; i++) {
                // 할인율이 기준 할인율보다 크면 구매
                if (salePercent[i] >= targetPercent) {
                    int price = (int) (emoticons[i] * (100-salePercent[i])/100);
                    total += price;
                }
            }
            // 총 구매 금액이 최대 금액보다 크면 가입
            if (total >= targetPrice) {
                tmpMember++;
            } else { // 아니면 그냥 구매
                tmpSell += total;
            }
        }
        // 현재 멤버가 기존 멤버와 같은 경우
        if (member == tmpMember) {
            // 판매 금액이 더 크다면 갱신
            if (sell < tmpSell) {
                member = tmpMember;
                sell = tmpSell;
            }
        // 현재 멤버가 더 많으면 갱신
        } else if (member < tmpMember) {
            member = tmpMember;
            sell = tmpSell;
        }
    }
}