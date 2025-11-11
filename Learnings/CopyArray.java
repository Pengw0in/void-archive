import java.util.Scanner;

public class CopyArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter array size: ");
        int n = sc.nextInt();
        
        int[] original = new int[n];
        int[] copy = new int[original.length];
        
        System.out.print("Enter elements: ");
        for (int i = 0; i < original.length; i++) {
            original[i] = sc.nextInt();
        }
        
        // Copy using length member
        for (int i = 0; i < original.length; i++) {
            copy[i] = original[i];
        }
        
        System.out.println("\nOriginal Array:");
        for (int i = 0; i < original.length; i++) {
            System.out.print(original[i] + " ");
        }
        
        System.out.println("\nCopied Array:");
        for (int i = 0; i < copy.length; i++) {
            System.out.print(copy[i] + " ");
        }
        
        sc.close();
    }
}