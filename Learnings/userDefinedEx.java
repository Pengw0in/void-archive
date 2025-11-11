import java.util.Scanner;

class NonComputers extends Exception {
    private String branch;

    NonComputers(String s) {
        branch = s;
    }
}

public class userDefinedEx {
    // Method that checks whether an exception is produced
    public static void Check(String a) throws NonComputers {
        if (a.equalsIgnoreCase("IT") || a.equalsIgnoreCase("CSE"))
            System.out.println("You Are in Computers");
        else
            throw new NonComputers(a);
    }

    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        String n;

        System.out.print("Enter Branch:");
        n = s.next();

        try {
            Check(n);
        } catch (NonComputers f) {
            System.out.println("Exception Occurred: Belongs to NON-COMPUTERS. Branch is " + n);
        }
    }
}
