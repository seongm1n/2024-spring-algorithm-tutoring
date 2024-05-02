import java.util.Scanner;

public class boj_5585 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        	int n = sc.nextInt();
		int money = 1000 - n;
		int result = 0;
		int[] changes = {500, 100, 50, 10, 5, 1};

		for (int i=0; i<changes.length; i++) {
			if (money%changes[i]>=0) {
				result += money/changes[i];
				money = money%changes[i];
			}
		}
		System.out.println(result);
	}
}
