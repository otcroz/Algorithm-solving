package recursion;

public class Recursion3_4 {

	public static void main(String[] args) {
		int data[] = { 1, 2, 3, 4, 5 };
		int res = search(data, 1, 4, 3);
		System.out.println(res);
	}

	public static int search(int data[], int begin, int end, int target) {
		if (begin > end)
			return -1;
		else {
			int middle = (end + begin) / 2;
			if (data[middle] == target)
				return middle;

			int index = search(data, begin, middle - 1, target);
			if (index != -1)
				return index;
			else
				return search(data, middle + 1, end, target);
		}
	}
}
