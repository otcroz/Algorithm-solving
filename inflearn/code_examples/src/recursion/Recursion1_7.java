package recursion;

public class Recursion1_7 {

	public static void main(String[] args) {
		double res = gcd(20, 4);
		System.out.println(res);
	}

	public static double gcd(int m, int n) {
		if (m < n) { 
			int tmp = m;
			m = n;
			n = tmp;
		}
		if (m % n == 0)
			return n;
		else
			return gcd(n, m % n);
	}

}
