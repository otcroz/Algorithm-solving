package recursion;

public class Recursion3_5 {

	public static void main(String[] args) {
		int data[] = {1,2,3,4,5};
		int res = findMax(data, 1, 4);
	}

	public static int findMax(int data[], int begin, int end) {
		if (begin == end)
			return data[begin];
		else
			return Math.max(data[begin], findMax(data, begin + 1, end));
	}

}
