class Solution {
    public long solution(int w, int h) {
        long answer = (long) w*h;
        
        // 최대공약수 구하기
        int a = w;
        int b = h;
    
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        long gcd = (long) a;
        
        long w2 = (long) w/gcd;
        long h2 = (long) h/gcd;
        
        long x = (w2+h2-1)*gcd;
        answer -= x;
        
        return answer;
    }
}