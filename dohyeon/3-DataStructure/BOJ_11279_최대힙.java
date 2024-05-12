package CMD_DataStructure;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.PriorityQueue;
import java.util.Comparator;

public class BOJ_11279 { // 최대 힙
    public static int[] solution(int N, int[] input, PriorityQueue<Integer> pq) {
        // 1. input 의 요소값이 0인 경우를 카운트 = countZero
        // 2. 입력값이 0이라면 배열의 최대 값을 삭제 후 -> 정답 배열에 저장 (poll)
        // 3. 입력값이 자연수라면 해당 값을 배열에 삽입(add)

        // 1
        int countZero = 0;
        for (int i = 0; i < N; i++) {
            if (input[i] == 0) {
                countZero++;
            }
        }

        int[] answer = new int[countZero];
        int index = 0;
        for (int i = 0; i < N; i++) {
            // 2
            if (input[i] == 0) {
                pq.add(input[i]);
                answer[index++] = pq.poll();
            }
            // 3
            else {
                pq.add(input[i]);
            }
        }
        return answer;
    }

    public static void main(String[] args) throws IOException {
        // 버퍼를 사용하여 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 정수형 우선순위 큐 생성(최소 힙) -> PriorityQueue<Integer>
        // 최대 힙으로 변경 -> Comparator.reverseOrder()
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        // 정수 N 입력
        int N = Integer.parseInt(br.readLine());
        // 입력값 저장
        int[] input = new int[N];
        for (int i = 0; i < N; i++) {
            input[i] = Integer.parseInt(br.readLine());
        }
        // 결과 출력
        int[] result = solution(N, input, pq);
        for (int i = 0; i < result.length; i++) {
            System.out.println(result[i]);
        }
    }
}
