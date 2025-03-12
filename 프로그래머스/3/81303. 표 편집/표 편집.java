import java.util.*;

class Solution {
    static class Node {
        Node prev = null;
        Node next = null;
        boolean isDelete = false;
    }
    public String solution(int n, int k, String[] cmd) {
        
        Node[] arr = new Node[n+1];
        // 첫번째 노드
        arr[0] = new Node();
        // 노드 연결
        for (int i=1; i<n; i++) {
            arr[i] = new Node();
            arr[i].prev = arr[i-1];
            arr[i-1].next = arr[i];
        }
        // 삭제 노드 보관
        Stack<Node> q = new Stack<>();
        
        Node now = arr[k];
        for (String command : cmd) {
            // 공백 기준 분리
            String[] c = command.split(" ");
            // 크기 1보다 크면 이동 명령
            if (c.length > 1) {
                // 칸 이동
                int cnt = Integer.parseInt(c[1]);
                if (c[0].equals("D")) {
                    for (int i=0; i<cnt; i++) {
                        now = now.next;
                    }
                } else {
                    for (int i=0; i<cnt; i++) {
                        now = now.prev;
                    }
                }
            } else {
                // 삭제
                if (c[0].equals("C")) {
                    now.isDelete = true;
                    q.push(now); // 휴지통에 넣고
                    
                    // 앞 뒤 노드 연결
                    Node prev = now.prev;
                    Node next = now.next;
                    // 맨 끝 행인 경우
                    if (next == null) {
                        prev.next = null;
                        now = prev;
                    } else if (prev == null) { // 맨 첫 행인 경우
                        next.prev = null;
                        now = next;
                    } else {
                        prev.next = next;
                        next.prev = prev;
                        now = next;
                    }
                } else {
                    // 복구
                    Node deleted = q.pop();
                    Node prev = deleted.prev;
                    Node next = deleted.next;
                    
                    deleted.isDelete = false;
                    
                    // 노드 다시 연결
                    if (prev != null) {
                        prev.next = deleted;
                    }
                    if (next != null) {
                        next.prev = deleted;
                    }
                }
            }
  
        }
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<n; i++) {
            if (arr[i].isDelete) {
                sb.append("X");
            } else {
                sb.append("O");
            }
        }
        
        return sb.toString();
    }
}