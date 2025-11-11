import java.util.Scanner;

public class ElementSearch {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        int[] arr = {10, 20, 30, 40, 50};
        System.out.print("Enter element to search: ");
        int search = s.nextInt();
        
        boolean found = false;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == search) {
                System.out.println("Element found at index " + i);
                found = true;
                break;
            }
        }
        
        if (!found) {
            System.out.println("Element not found in the array");
        }
    }
}