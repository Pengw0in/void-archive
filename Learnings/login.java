import java.util.Scanner;

public class login {
    public static void main(String[] args) {
        int password = 3243524;
        Scanner s = new Scanner(System.in);
        int user_pass;

        for (int i = 0; i < 3; i++) {
            System.out.print("Enter your password: ");
            user_pass = s.nextInt();

            if (user_pass == password) {
                System.out.print("Login successful");
                System.exit(0);
            }
            if (i < 2) {
                System.out.println("Try again");
            }
        }
        System.out.println("Account locked");
        s.close();
    }
}
