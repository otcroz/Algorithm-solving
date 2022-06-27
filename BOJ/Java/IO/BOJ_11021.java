package IO;

import java.util.Scanner;

public class BOJ_11021 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int rep = s.nextInt();

		for (int i = 0; i < rep; i++) {
			int a = s.nextInt();
			int b = s.nextInt();
			int res = a+b;

			System.out.println("Case #" + (i + 1) + ": " + res);
			// String이랑 같이 계산하면 문자열이 되네 => 괄호로 묶는 방법
		}

	}

}
