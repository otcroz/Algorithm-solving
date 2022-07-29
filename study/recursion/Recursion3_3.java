package recursion;

public class Recursion3_3 {

	public static void main(String[] args) {
		int data[] = { 1, 2, 3, 4, 5 };
		int res = search(data, 2, 5, 3);
		System.out.println(res);
	}

	public static int search(int data[], int begin, int end, int target) {
		if (begin > end)
			return -1;
		else if (target == data[end])
			return end;
		else
			return search(data, begin, end - 1, target);
	}

}
