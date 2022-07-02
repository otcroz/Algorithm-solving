package recursion;

public class Recursion1_2 {
	public static void main(String[] args) {
		int n = 4;
		func(n);
	}
	
	public static void func(int k) {
		if(k == 0) {
			return; 
		}
		else {
			System.out.println("Hello Otcr ~ !");
			func(k-1);
		}
	}
}
