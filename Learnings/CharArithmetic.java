import java.util.Scanner;

public class CharArithmetic {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        char char1, char2;
        
        System.out.print("Enter first character: ");
        char1 = input.next().charAt(0);
        
        System.out.print("Enter second character: ");
        char2 = input.next().charAt(0);
        
        System.out.println("Addition: " + (char1 + char2));
        System.out.println("Subtraction: " + (char1 - char2));
        System.out.println("Multiplication: " + (char1 * char2));
        System.out.println("Division: " + (char1 / char2));
        String line = "hi how are yoy, are you fine?";
        System.out.println(line.contains("hi"));
        input.close();
    }
}


