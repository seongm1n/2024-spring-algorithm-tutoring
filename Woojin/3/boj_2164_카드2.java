import java.util.Scanner;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int deck = sc.nextInt();
        Queue<Integer> q = new LinkedList<>();

        for(int i = 1; i<=deck; i++){
            q.add(i);
        }
        while(q.size() != 1){
            q.remove();
            q.add(q.poll());
        }
        int answer = q.element();
        System.out.println(answer);
    }
}
