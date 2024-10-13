import java.util.*;

class Block {
    int r;
    int c;
    
    public Block(int r, int c) {
        this.r = r;
        this.c = c;
    }
}

class Solution {
    static int answer = 0;
    static char[][] boards;
    public int solution(int m, int n, String[] board) {
        boards = new char[m][n];
        
        for (int i=0; i<m; i++) {
            boards[i] = board[i].toCharArray();
        }
        while (true) {
            // 제거가능 블록 찾기
            List<Block> blocks = checkBlock(m, n);
            // 없으면 종료
            if (blocks.isEmpty()) break;
            // 블록 제거
            for (Block b : blocks) {
                remove(b);
            }
            move(m, n);
        }
        
        return answer;
    }
    // 제거 가능한 블록 좌표 리스트 반환
    public List<Block> checkBlock(int m, int n) {
        List<Block> removeBlock = new ArrayList<>();
        
        for (int i=0; i<m-1; i++) {
            for (int j=0; j<n-1; j++) {
                char c = boards[i][j];
                // 같은 블록 네개 모여있는지 확인
                if (c != '-' && boards[i+1][j] == c &&
                   boards[i][j+1] == c &&
                   boards[i+1][j+1] == c) {
                    removeBlock.add(new Block(i, j));
                } 
            }
        }
        return removeBlock;
    }
    // 블록제거 후 카운트
    public void remove(Block b) {
        int r = b.r;
        int c = b.c;
        for (int i=r; i<=r+1; i++) {
            for (int j=c; j<=c+1; j++) {
                // -로 바꾸고 카운트
                if (boards[i][j] != '-') {
                    boards[i][j] = '-';
                    answer++;
                }
            }
        }
    }
    // 제거된 만큼 블록 이동
    public void move(int m, int n) {
        for (int j=0; j<n; j++) {
            for (int i=m-1; i>=0; i--) {
                if (boards[i][j] == '-') {
                    for (int k=i-1;k>=0;k--) {
                        if (boards[k][j] != '-') {
                            boards[i][j] = boards[k][j];
                            boards[k][j] = '-';
                            break;
                        }
                    }
                }
            }
        }
        
    }
}