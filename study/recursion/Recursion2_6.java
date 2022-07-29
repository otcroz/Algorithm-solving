package recursion;

import java.util.Scanner;

public class Recursion2_6 {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int data[] = {0};
		readFrom(5, data, s);
	}
	public static void readFrom(int n, int data[], Scanner in ) {
		if(n==0) return;
		else {
			readFrom(n-1, data, in);
			data[n-1] = in.nextInt();
		}
	}
}
