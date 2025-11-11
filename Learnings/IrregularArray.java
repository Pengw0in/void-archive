import java.util.Scanner;

public class IrregularArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter number of rows: ");
        int rows = sc.nextInt();
        
        int[][] arr = new int[rows][];
        
        for (int i = 0; i < rows; i++) {
            System.out.print("Enter number of columns for row " + (i+1) + ": ");
            int cols = sc.nextInt();
            arr[i] = new int[cols];
            
            System.out.print("Enter elements: ");
            for (int j = 0; j < cols; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        
        System.out.println("\nIrregular Array:");
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        
        sc.close();
    }
}