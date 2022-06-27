package IO;

import java.util.Scanner;

public class BOJ_10950 {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int repeat = s.nextInt();
		
		//  นÝบน
		for(int i = 0; i<repeat; i++) {
			int a =  s.nextInt();
			int b = s.nextInt();
			System.out.println(a+b);
		}
		
	}
}
