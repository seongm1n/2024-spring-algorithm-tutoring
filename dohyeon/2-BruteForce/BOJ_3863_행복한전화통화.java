package CMD_BruteForce;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class BOJ_3863 {
    public static int[] solution(int[] callStart, int[] callDur, int[] tapStart, int[] tapDur, int N, int M) {
        int[] answer = new int[M];
        
        // 도청 시간대가 겹치는지 확인
        for (int i = 0; i < M; i++) {
            int count = 0;
            for (int j = 0; j < N; j++) {
                if (tapStart[i] < (callStart[j] + callDur[j]) && (tapStart[i] + tapDur[i]) > callStart[j]) {
                    count += 1;
                }
            }
            answer[i] = count;
        }
        return answer;
    }

    public static void main(String[] args) throws IOException {
        // 버퍼를 사용하여 입력받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            // 문자열로 한 줄 읽고
            String nm = br.readLine();
            // 공백 기준으로 나누어
            StringTokenizer nmToken = new StringTokenizer(nm, " ");
            // 1. 정수형으로 형변환하여 N과 M에 저장
            int N = Integer.parseInt(nmToken.nextToken()); // 전화통화 횟수
            int M = Integer.parseInt(nmToken.nextToken()); // 도청 횟수

            if (N == 0 && M == 0) {
                break;
            }

            int[] source = new int[N];
            int[] dest = new int[N];
            int[] callStart = new int[N];
            int[] callDur = new int[N];
            
            // 2. Source, Destination, Start, Duration 입력
            for (int i = 0; i < N; i++) {
                String call = br.readLine();
                StringTokenizer callToken = new StringTokenizer(call, " ");

                source[i] = Integer.parseInt(callToken.nextToken());
                dest[i] = Integer.parseInt(callToken.nextToken());
                callStart[i] = Integer.parseInt(callToken.nextToken());
                callDur[i] = Integer.parseInt(callToken.nextToken());
            }

            int[] tapStart = new int[M];
            int[] tapDur = new int[M];
            
            // 3. tapStart, tapDur 입력
            for (int i = 0; i < M; i++) {
                String tap = br.readLine();
                StringTokenizer tapToken = new StringTokenizer(tap, " ");

                tapStart[i] = Integer.parseInt(tapToken.nextToken());
                tapDur[i] = Integer.parseInt(tapToken.nextToken());
            }
            
            // 결과값 출력
            int[] result = solution(callStart, callDur, tapStart, tapDur, N, M);
            
            for (int i = 0; i < result.length; i++) {
                System.out.println(result[i]);
            }
        }
    }
}
