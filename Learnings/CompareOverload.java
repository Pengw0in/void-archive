import java.util.Scanner;

public class CompareOverload {
    
    public void compare(int a, int b) {
        if (a > b) {
            System.out.println("Greater integer: " + a);
        } else if (b > a) {
            System.out.println("Greater integer: " + b);
        } else {
            System.out.println("Both integers are equal: " + a);
        }
    }
    
    public void compare(char a, char b) {
        if (a > b) {
            System.out.println("Greater character: " + a);
        } else if (b > a) {
            System.out.println("Greater character: " + b);
        } else {
            System.out.println("Both characters are equal: " + a);
        }
    }
    
    public void compare(String a, String b) {
        int result = a.compareTo(b);
        if (result > 0) {
            System.out.println("Greater string: " + a);
        } else if (result < 0) {
            System.out.println("Greater string knj: " + b);
        } else {
            System.out.println("Both strings are equal: " + a);
        }
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        CompareOverload obj = new CompareOverload();
        
        System.out.print("Enter first integer: ");
        int num1 = input.nextInt();
        System.out.print("Enter second integer: ");
        int num2 = input.nextInt();
        obj.compare(num1, num2);
        
        System.out.print("Enter first character: ");
        char char1 = input.next().charAt(0);
        System.out.print("Enter second character: ");
        char char2 = input.next().charAt(0);
        obj.compare(char1, char2);
        
 
        input.nextLine();
        System.out.print("Enter first string: ");
        String str1 = input.nextLine();
        System.out.print("Enter second string: ");
        String str2 = input.nextLine();
        obj.compare(str1, str2);
        
        input.close();
    }
}
