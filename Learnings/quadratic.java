import java.util.Scanner;

public class quadratic {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        double a, b, c;
        
        System.out.print("Enter coefficient a: ");
        a = s.nextDouble();
        
        if (a == 0) {
            System.out.println("This is not a quadratic equation (a cannot be 0)");
        } else {
            System.out.print("Enter coefficient b: ");
            b = s.nextDouble();
            System.out.print("Enter coefficient c: ");
            c = s.nextDouble();
            
            double discriminant = b * b - 4 * a * c;
            
            if (discriminant > 0) {
                double root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
                double root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
                System.out.println("Two real and distinct roots:");
                System.out.println("Root 1 = " + root1);
                System.out.println("Root 2 = " + root2);
            } else if (discriminant == 0) {
                double root = -b / (2 * a);
                System.out.println("One real root (repeated):");
                System.out.println("Root = " + root);
            } else {
                double realPart = -b / (2 * a);
                double imaginaryPart = Math.sqrt(-discriminant) / (2 * a);
                System.out.println("Two complex roots:");
                System.out.println("Root 1 = " + realPart + " + " + imaginaryPart + "i");
                System.out.println("Root 2 = " + realPart + " - " + imaginaryPart + "i");
            }
        }
        
        s.close();
    }
}
