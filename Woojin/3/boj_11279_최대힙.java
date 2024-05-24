import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
      
        //우선순위큐 = PriorityQueue, Collections.reverseOrder() 내림차순 정렬
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
      
        //값을 입력해 두는 곳(Scanner 소요시간이 많이 걸리는거 대비)
        StringBuilder sb = new StringBuilder();

        //N번 만큼 반복
        for(int i = 0; i < N; i++){
            int x = sc.nextInt();

            //0일 경우 최고값 출력 후 제거
            if(x == 0){
              
                //비어있으면 답에 0추가
                if(pq.isEmpty()){
                    sb.append(0).append("\n");
                }
                  
                //비어있지 않으면 답에 최고값(내림차순으로 해서 맨 처음에 위치 poll 이용) 추가
                else{
                    sb.append(pq.poll()).append("\n");
                }
            }
              
            //0이 아닐경우 추가
            else{
                pq.add(x);
            }
        }
      
        //모아둔 값을 출력
        System.out.println(sb);
    }
}
