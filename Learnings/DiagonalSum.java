import java.util.Scanner;

public class DiagonalSum {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        System.out.print("Enter matrix size: ");
        int n = s.nextInt();
        int[][] matrix = new int[n][n];
        
        System.out.println("Enter matrix elements:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = s.nextInt();
            }
        }
        
        int primarySum = 0, secondarySum = 0;
        
        for (int i = 0; i < n; i++) {
            primarySum += matrix[i][i];           // Primary diagonal
            secondarySum += matrix[i][n - 1 - i]; // Secondary diagonal
        }
        
        System.out.println("Primary diagonal sum: " + primarySum);
        System.out.println("Secondary diagonal sum: " + secondarySum);
        s.close();
    }
}