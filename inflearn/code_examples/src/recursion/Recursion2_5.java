package recursion;

public class Recursion2_5 {

	public static void main(String[] args) {
		int data[] = { 1, 2, 3, 4, 5 };
		int res = sum(5, data);
		System.out.println(res);

	}

	public static int sum(int n, int data[]) {
		if (n <= 0)
			return 0;
		else
			return sum(n - 1, data) + data[n - 1];
	}

}
