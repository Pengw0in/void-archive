import java.util.Scanner;

public class rightTri {
    public static void main(String[] args) {
        int number;
        Scanner s = new Scanner(System.in);

        System.out.print("Input number of rows: ");
        number = s.nextInt();

        for (int i = 1; i <= number; i++) {
            for (int j = 1; j < i + 1; j++ ) {
                System.out.print(j);
            }
            System.out.print("\n");
        }
        s.close();
    }
}
