package recursion;

public class Recursion2_1 {

	public static void main(String[] args) {
		int res = length("abcd");
		System.out.println(res);
	}

	public static int length(String str) {
		if (str.equals(""))
			return 0;
		else
			return 1 + length(str.substring(1));
	}

}
