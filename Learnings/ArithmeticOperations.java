import java.util.Scanner;

public class ArithmeticOperations {
    
    public static double add(double a, double b) {
        return a + b;
    }
    
    public static double subtract(double a, double b) {
        return a - b;
    }
    
    public static double multiply(double a, double b) {
        return a * b;
    }
    
    public static double divide(double a, double b) {
        if (b != 0) {
            return a / b;
        } else {
            System.out.println("Error: Division by zero!");
            return 0;
        }
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double num1, num2;
        
        System.out.print("Enter first number: ");
        num1 = input.nextDouble();
        
        System.out.print("Enter second number: ");
        num2 = input.nextDouble();
        
        System.out.println("Addition: " + add(num1, num2));
        System.out.println("Subtraction: " + subtract(num1, num2));
        System.out.println("Multiplication: " + multiply(num1, num2));
        System.out.println("Division: " + divide(num1, num2));
        
        input.close();
    }
}