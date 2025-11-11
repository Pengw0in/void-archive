import java.util.Arrays;
import static java.lang.System.out;

public class moreMethods {
    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5};
        int arr1[] = {1,2,3,4,5};
        int[][] arr2 = {{1, 2}, {3, 4}};
        int[][] arr3 = {{1, 2}, {3, 5}};
        int key = 5;
        int index = Arrays.binarySearch(arr, key);
        boolean letsee = Arrays.deepEquals(arr2, arr3);
        int arr4[] = new int[5];
        Arrays.se
        Arrays.fill(arr4, 5);
        out.println(Arrays.toString(arr4));
        out.println(index);
    }
}
