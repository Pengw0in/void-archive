import java.io.*;

public class StudentAverage {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Enter number of students: ");
        int n = Integer.parseInt(br.readLine());

        String[] names = new String[n];
        int[] marks = new int[n];
        int sum = 0;

        for (int i = 0; i < n; i++) {
            System.out.print("Enter name of student " + (i + 1) + ": ");
            names[i] = br.readLine();

            System.out.print("Enter marks of " + names[i] + ": ");
            marks[i] = Integer.parseInt(br.readLine());

            sum += marks[i];
        }

        double average = (double) sum / n;
        System.out.println("Average marks of the class: " + average);
    }
}