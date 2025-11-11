import java.util.Scanner;

public class multiptable {
    public static void main(String[] args) {
        int num;
        System.out.print("Enter the number: ");
        Scanner s = new Scanner(System.in);
        num = s.nextInt();

        for (int i = 0; i < 11 ; i ++) {
            System.out.println( num + " x " + i + " = " + i * num);
        }
        s.close();
    }
}
