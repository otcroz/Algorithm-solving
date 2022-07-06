package recursion;

public class Recursion1_6 {

	public static void main(String[] args) {
		int res = fibonacci(4);
		System.out.println(res);
	}

	public static int fibonacci(int n) {
		if (n < 2)
			return n;
		else
			return fibonacci(n - 1) + fibonacci(n - 2);
	}

}
