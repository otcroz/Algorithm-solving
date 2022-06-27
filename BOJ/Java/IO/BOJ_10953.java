package IO;

import java.util.Scanner;

public class BOJ_10953 {

	public static void main(String[] args) {
		String[] arr = new String[1];
		String[] num = new String[2];
		
		Scanner s = new Scanner(System.in);
		int rep = s.nextInt();
		
		for(int i=0; i<rep; i++) {
			String str = s.next();
			arr[0] = str;
			num = arr[0].split(",");
			
			int a = Integer.parseInt(num[0]);
			int b = Integer.parseInt(num[1]);
			
			System.out.println(a+b);
		}
			

	}

}
