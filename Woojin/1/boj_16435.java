import java.util.Scanner;
import java.util.Arrays;

public class boj_16435 {
	public static void main(String[] args) {		
		int N, L;
		
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		L = sc.nextInt();
		int[] h = new int[N];
		
		for (int i = 0; i < N; i++) {
			h[i] = sc.nextInt();
		}
		
		//오름차순
		Arrays.sort(h);
		
		for (int i = 0; i < N; i++) {
			if (h[i] <= L) {
				L += 1;
			}
		}
		System.out.println(L);
	}
}
