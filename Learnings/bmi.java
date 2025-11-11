import java.util.Scanner;

public class bmi {
    public static void main(String[] args) {
        double user_bmi;
        double height;
        double weight;

        Scanner input = new Scanner(System.in);

        System.out.print("Enter your height(meters): ");
        height = input.nextDouble();
        System.out.print("Enter your weight(kg): ");
        weight = input.nextDouble();

        user_bmi = weight / (height * height);

        if (user_bmi < 18.5) {
            System.out.println("your BMI is " + user_bmi + ", Type: Underweight");
        } else if (user_bmi >= 18.5 && user_bmi < 25.0) {
            System.out.println("your BMI is " + user_bmi + ", Type: Normal");
        } else if (user_bmi >= 25.0 && user_bmi < 30.0) {
            System.out.println("your BMI is " + user_bmi + ", Type: Overweight");
        } else {
            System.out.println("your BMI is " + user_bmi + ", Type: Overweight");
        }

        input.close();

    }
}