import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String s = sc.next();
        int answer = -1;
        char[] c = new char[N];
        
        //String 을 char 로 변환
        for(int i = 0; i < s.length(); i++){
            c[i] = s.charAt(i);
        }
        
        //Stack
        Stack<Character> stack = new Stack<>();
        for(int i = 0; i < N; i++){
            //stack 비어있거나 stack 맨 위와 현재가 같으면 추가
            if(stack.isEmpty() || stack.peek() == c[i]){
                stack.push(c[i]);
            }
            
            //stack 맨 위와 현재가 다르면 삭제
            else{
                stack.pop();
            }
            
            //답
            if(answer < stack.size())
                answer = stack.size();
        }
        
        //문자열 만들 수 없음
        if(!stack.isEmpty() || N % 2 != 0){
            answer = -1;
        }
        System.out.println(answer);
    }
}
