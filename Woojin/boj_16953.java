package boj_16953;
import java.util.Scanner;

public class boj_16953 {
	public static void main(String[] args) {
		int A, B;
		Scanner sc = new Scanner(System.in);
		A = sc.nextInt();
		B = sc.nextInt();
		int turn = 1;
		while(A != B) {
			if (A>B) {
				break;
			}
			else if(B % 2 == 0) {
				B /= 2;
				turn += 1;
			}
			else if(B % 10 == 1) {
				B -= 1;
				B /= 10;
				turn += 1;
			}
			else {
				break;
			}
		}
		if (A == B) {
			System.out.println(turn);
		}
		else {
			System.out.println("-1");
		}
	}
}
