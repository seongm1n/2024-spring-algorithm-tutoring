import java.util.Scanner;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] N = new int[9];
		int sum = 0;
		
		for(int i = 0; i < 9; i++) {
			N[i] = sc.nextInt();
			sum += N[i];
		}
		for (int i = 0; i < 8; i++) {
			for(int j = i+1; j < 9; j++) {
				if(sum - N[i] - N[j] == 100) {
					N[i] = 0;
					N[j] = 0;
					Arrays.sort(N);
					for(int k = 2; k < 9; k++) {
						System.out.println(N[k]);
					}
                    return;
				}
			}
		}
	}
}
