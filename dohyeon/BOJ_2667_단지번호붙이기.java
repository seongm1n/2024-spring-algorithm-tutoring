package cmd_dfsbfs;

import java.io.*;
import java.util.*;

public class BOJ_2667_단지번호붙이기 {
    // solution 전역변수
    static int count;
    static List<Integer> answer;
    // dfs 전역변수
    static int[]dx = {0, 0, -1, 1};
    static int[]dy = {-1, 1, 0, 0};
    static boolean[][] visited;
    // main 전역변수
    static int n;
    static int[][] input;

    // 1. 모든 입력 값들을 하나씩 검사
    // 2. 현재 위치의 값이 1이고 아직 방문하지 않은 경우
    // -> dfs 시작
    // 3. 현재 위치부터 상하좌우 부분 검사
    // 4. 해당 위치에 집이 있고, 단지 크기를 벗어나지 않았고 && 방문하지 않았을 때
    // -> 단지 수로 카운트, 재귀를 통해 연결된 집 방문
    // 5. 모두 검사하였다면 오름차순 정렬 후 정답 반환
    private static List<Integer> solution(int n, int[][] input) {
        answer = new LinkedList<>();

        // 1
        count = 1;
        for(int i = 0; i < n ; i++){
            for(int j = 0; j < n; j++){
                // 2
                if(input[i][j] == 1 && !visited[i][j]){
                    dfs(i, j);
                    answer.add(count);
                    count = 1;
                }
            }
        }
        // 5
        Collections.sort(answer);
        return answer;
    }

    private static void dfs(int x, int y) {
        visited[x][y] = true;

        // 3
        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            // 4
            if(input[nx][ny] == 1 && nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]){
                count++;
                dfs(nx, ny);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // n 입력
        n = Integer.parseInt(br.readLine());
        // 총 단지 입력
        visited = new boolean[n][n];
        input = new int[n][n];
        for(int i = 0; i < n; i++) {
            String line = br.readLine();
            for(int j = 0; j < n; j++) {
                input[i][j] = Integer.parseInt(String.valueOf(line.charAt(j)));
            }
        }
        // 결과 출력
        List<Integer> result = solution(n, input);
        System.out.println(result.size());
        for (int i : result) {
            System.out.println(i);
        }
    }
}
