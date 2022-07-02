package recursion;

public class Recursion2_3 {

	public static void main(String[] args) {
		printCharReverse("otcrotcr");

	}
	
	public static void printCharReverse(String str) {
		if(str.length() == 0) return;
		else {
			printCharReverse(str.substring(1));
			System.out.println(str.charAt(0));
		}
	}

}
