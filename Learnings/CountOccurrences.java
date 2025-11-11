import java.util.Scanner;

public class CountOccurrences {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        int[] arr = {1, 2, 3, 2, 4, 2, 5};
        System.out.print("Enter number to count: ");
        int target = s.nextInt();
        
        int count = 0;
        for (int num : arr) {
            if (num == target) {
                count++;
            }
        }
        
        System.out.println("Number " + target + " occurs " + count + " times");
    }
}