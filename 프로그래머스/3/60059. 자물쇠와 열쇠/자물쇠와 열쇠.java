import java.util.*;

class Solution {
    static int[][] arr;
    public boolean solution(int[][] key, int[][] lock) {
        
        // 배열 확장
        int l = key.length * 2 + lock.length - 2;
        arr = new int[l][l];
        // 자물쇠 표시
        for (int i=key.length-1; i<key.length+lock.length-1; i++) {
            for (int j=key.length-1; j<key.length+lock.length-1; j++) {
                arr[i][j] = lock[i-key.length+1][j-key.length+1];
            }
        }
        // 회전시키면서 매칭 확인
        for (int i=0; i<4; i++) {
            if (match(key, l)) {
                return true;
            } else {
                key = rotate(key);
            }
        }
        return false;
    }
    // 잠금 해제 확인
    public boolean match(int[][] key, int l) {
        int keyLen = key.length;
        for (int i=0; i<=l-keyLen; i++) {
            for (int j=0; j<=l-keyLen; j++) {
                // 키 넣기
                for (int x=0; x<keyLen; x++) {
                    for (int y=0; y<keyLen; y++) {
                        arr[i+x][j+y] += key[x][y];
                    }
                }
                // 잠금 해제 확인
                boolean unlock = true;
                for (int x=keyLen-1; x<=l-keyLen; x++) {
                    for (int y=keyLen-1; y<=l-keyLen; y++) {
                        if (arr[x][y] != 1) {
                            unlock = false;
                            break;
                        }
                    }
                    if (!unlock) break;
                }
                if (unlock) return true;
                // 키 빼기
                for (int x=0; x<keyLen; x++) {
                    for (int y=0; y<keyLen; y++) {
                        arr[i+x][j+y] -= key[x][y];
                    }
                }
            }
        }
        return false;
    }
    // key 시계방향 90도 회전
    public int[][] rotate(int[][] key) {
        int l = key.length;
        int[][] tmp = new int[l][l];
        
        for (int i = 0; i < l; i++) {
            for (int j = 0; j < l; j++) {
                tmp[j][l - i - 1] = key[i][j];
            }
        }
        
        return tmp;
        
    }
}