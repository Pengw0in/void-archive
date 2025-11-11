import java.util.Scanner;

public class StringMethods {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter a string: ");
        String str = sc.nextLine();
        
        System.out.println("\n=== STRING METHODS ===");
        System.out.println("Original String: \"" + str + "\"");
        System.out.println("Length: " + str.length());
        System.out.println("Uppercase: " + str.toUpperCase());
        System.out.println("Lowercase: " + str.toLowerCase());
        System.out.println("Trim: \"" + str.trim() + "\"");
        
        if (str.length() > 0) {
            System.out.println("First character: " + str.charAt(0));
        }
        
        System.out.println("Index of 'a': " + str.indexOf('a'));
        System.out.println("Last index of 'a': " + str.lastIndexOf('a'));
        System.out.println("Contains 'test': " + str.contains("test"));
        System.out.println("Starts with 'H': " + str.startsWith("H"));
        System.out.println("Ends with 'o': " + str.endsWith("o"));
        System.out.println("Replace 'a' with 'X': " + str.replace('a', 'X'));
        
        if (str.length() >= 3) {
            System.out.println("Substring (1,3): " + str.substring(1, 3));
        }
        
        System.out.println("Equals 'hello': " + str.equals("hello"));
        System.out.println("Equals ignore case 'HELLO': " + str.equalsIgnoreCase("HELLO"));
        System.out.println("Compare to 'apple': " + str.compareTo("apple"));
        System.out.println("Is empty: " + str.isEmpty());
        
        String[] words = str.split(" ");
        System.out.println("Split by space: " + java.util.Arrays.toString(words));
        
        sc.close();
    }
} 