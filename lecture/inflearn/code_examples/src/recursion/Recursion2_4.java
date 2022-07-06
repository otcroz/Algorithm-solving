package recursion;

public class Recursion2_4 {

	public static void main(String[] args) {
		printInBinary(4);
	}

	public static void printInBinary(int n) {
		if (n < 2)
			System.out.println(n);
		else {
			printInBinary(n / 2);
			System.out.println(n % 2);
		}
	}
}
