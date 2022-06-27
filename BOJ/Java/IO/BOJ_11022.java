package IO;

import java.util.Scanner;

public class BOJ_11022 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);

		int rep = s.nextInt();

		for (int i = 0; i < rep; i++) {
			int a = s.nextInt();
			int b = s.nextInt();
			int res = a + b;

			System.out.println("Case #" + (i + 1) + ": " + a + " + " + b + " = " + res);
		}

	}

}
