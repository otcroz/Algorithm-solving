package recursion;

public class Recursion3_6 {

	public static void main(String[] args) {
		int data[] = {1,2,3,4,5};
		int res = findMax(data, 1, 4);

	}
	
	public static int findMax(int data[], int begin, int end) {
		if(begin == end)
			return data[begin];
		else {
			int middle = (begin+end) / 2;
			int max1 = findMax(data, begin, middle);
			int max2 = findMax(data, middle+1, end);
			return Math.max(max1,  max2);		
		}
	}

}
