import java.io.*;

public class SumOfNumbers {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Enter how many numbers: ");
        int n = Integer.parseInt(br.readLine());

        int sum = 0;
        for (int i = 1; i <= n; i++) {
            System.out.print("Enter number " + i + ": ");
            int num = Integer.parseInt(br.readLine());
            sum += num;
        }

        System.out.println("Sum = " + sum);
    }
}