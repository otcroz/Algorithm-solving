package recursion;

public class Recursion3_1 {

	public static void main(String[] args) {
		int data[] = {1,2,3,4,5};
		int res = search(data, 5,5);
		System.out.println(res);
	}
	
	static int search(int data[], int n, int target) {
		for(int i=0; i<n; i++) {
			if (data[i] == target)
				return i;
		}
		return -1;
	}

}
