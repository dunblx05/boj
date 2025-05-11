import java.util.*;

class Solution {
    static int[][] map = new int[102][102];
    static boolean[][] visited = new boolean[102][102];
    // 상, 우, 하, 좌
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int answer = 0;
    
    private static class Pos {
        int x;
        int y;
        int dist;
        
        public Pos(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
        
    }
    
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        // 1로 칠하기
        for(int[] rec : rectangle) {
            int x1 = rec[0] * 2;
            int y1 = rec[1] * 2;
            int x2 = rec[2] * 2;
            int y2 = rec[3] * 2;
            
            for(int i = x1; i <= x2; i++) {
                for(int j = y1; j <= y2; j++) {
                    map[i][j] = 1;
                }
            }
            
        }
        // 내부 제거
        for(int[] rec : rectangle) {
            int x1 = rec[0] * 2;
            int y1 = rec[1] * 2;
            int x2 = rec[2] * 2;
            int y2 = rec[3] * 2;
            
            for(int i = x1 + 1; i < x2; i++) {
                for(int j = y1 + 1; j < y2; j++) {
                    map[i][j] = 0;
                }
            }
            
        }
        
        bfs(characterX * 2, characterY * 2, itemX * 2, itemY * 2);
        
        return answer / 2;
    }
    
    private static void bfs(int startX, int startY, int itemX, int itemY) {
        Deque<Pos> q = new ArrayDeque<>();
        q.addLast(new Pos(startX, startY, 0));
        visited[startX][startY] = true;
        
        while(!q.isEmpty()) {
            Pos curPos = q.removeFirst();
            
            if(curPos.x == itemX && curPos.y == itemY) {
                answer = curPos.dist;
                return;
            }
        
            for(int i = 0; i < 4; i++) {
                int nx = curPos.x + dx[i];
                int ny = curPos.y + dy[i];
                int ndist = curPos.dist;
                
                if(nx < 0 || ny < 0 || nx >= 102 || ny >= 102) {
                    continue;
                }
                
                if(visited[nx][ny] == true) {
                    continue;
                }
                
                if(map[nx][ny] == 1) {
                    visited[nx][ny] = true;
                    q.addLast(new Pos(nx, ny, ndist + 1));
                    
                }
                
            }
            
        }
        
    }
    
}