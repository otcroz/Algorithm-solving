package recursion;

public class Recursion3_7 {

	public static void main(String[] args) {
		String[] data = {"a","b","c","d","e"};
		int res = binarySearch(data, "s", 2, 3);

	}

	public static int binarySearch(String[] data, String target, int begin, int end) {
		if (begin > end)
			return -1;
		else {
			int middle = (begin + end) / 2;
			int compResult = target.compareTo(data[middle]);

			if (compResult == 0)
				return middle;
			else if (compResult < 0)
				return binarySearch(data, target, begin, middle - 1);
			else
				return binarySearch(data, target, middle + 1, end);

		}
	}

}
