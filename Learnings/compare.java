import java.util.Scanner;

public class compare {
public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        double a, b;
        
        System.out.print("Enter a: ");
        a = s.nextDouble();
        double aTrucated = (long) (a * 1000) / 1000.00;

        System.out.print("Enter b: ");
        b = s.nextDouble();
        double bTrucated = (long) (b * 1000) / 1000.00;

        if ( aTrucated == bTrucated) {
            System.out.println("same up to three decimal places");
        } else {
            System.out.println("not same up to three decimal places");
        }

        s.close();
    }
}
