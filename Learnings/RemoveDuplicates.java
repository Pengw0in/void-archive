import java.util.Scanner;

public class RemoveDuplicates {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int[] arr = new int[5];
        System.out.print("Enter 5 elements: ");
        for (int i = 0; i < 5; i++) {
            arr[i] = sc.nextInt();
        }
        
        System.out.println("\nOriginal Array:");
        for (int i = 0; i < 5; i++) {
            System.out.print(arr[i] + " ");
        }
        
        // Remove duplicates
        int[] unique = new int[5];
        int uniqueCount = 0;
        
        for (int i = 0; i < 5; i++) {
            boolean isDuplicate = false;
            for (int j = 0; j < uniqueCount; j++) {
                if (arr[i] == unique[j]) {
                    isDuplicate = true;
                    break;
                }
            }
            if (!isDuplicate) {
                unique[uniqueCount++] = arr[i];
            }
        }
        
        System.out.println("\nArray after removing duplicates:");
        for (int i = 0; i < uniqueCount; i++) {
            System.out.print(unique[i] + " ");
        }
        
        sc.close();
    }
}