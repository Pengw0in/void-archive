// 3x4 matrix row and column sum
import java.util.Scanner;

public class MatrixSum {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int[][] matrix = new int[3][4];
        
        System.out.println("Enter 3x4 matrix elements:");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 4; j++) {
                matrix[i][j] = s.nextInt();
            }
        }
        
        // Row sums
        for (int i = 0; i < 3; i++) {
            int rowSum = 0;
            for (int j = 0; j < 4; j++) {
                rowSum += matrix[i][j];
            }
            System.out.println("Row " + (i + 1) + " sum: " + rowSum);
        }
        
        // Column sums
        for (int j = 0; j < 4; j++) {
            int colSum = 0;
            for (int i = 0; i < 3; i++) {
                colSum += matrix[i][j];
            }
            System.out.println("Column " + (j + 1) + " sum: " + colSum);
        }
    }
}