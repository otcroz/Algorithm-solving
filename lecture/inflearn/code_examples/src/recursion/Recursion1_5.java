package recursion;

public class Recursion1_5 {

	public static void main(String[] args) {
		double res = power(4, 2);
		System.out.println(res);
	}
	
	public static double power(double x, int n) {
		if(n == 0) return 1;
		else return x * power(x, n-1);
	}

}
