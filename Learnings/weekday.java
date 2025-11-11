import java.util.Scanner;

public class weekday {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        int today;
        System.out.print("Enter today's day: ");
        today = s.nextInt();

        int future;
        System.out.print("Enter the number of days elapsed since today: ");
        future = s.nextInt();

        if (today + future >= 7) {
            future = (today + future) - 7;
        }

        System.out.println("Today is " + day(today) +" and the future day is " + day(future));
        s.close();
    }

    public static String day(int day) {
        switch (day) {
            case 1:
                return "Monday";
            case 2:
                return "Tuesday";
            case 3:
                return "Wednesday";
            case 4:
                return "Thrusday";
            case 5:
                return "Friday";
            case 6:
                return "Saturday";
            case 7:
                return "Sunday";
            default:
                return "Invalid Day";
        }
    }
}
