import java.util.Random;
import java.util.Scanner;
import java.util.Arrays;

public class lottery {
    public static void main(String[] args) {
        int Guess;
        int lotteryNum = 0;
        int temp;

        Random r = new Random();
        int[] twoDigitNum = {r.nextInt(9), r.nextInt(9)};

        Scanner s = new Scanner(System.in);
        System.out.print("Enter a your Guess(two-digit Number): ");
        Guess = s.nextInt();

        int[] guessArray = new int[2];

        for (int i = 2; i > 0; i-- ){
            temp = Guess % 10;
            guessArray[i-1] = temp;
            Guess /= 10;
        }

        if (Arrays.equals(guessArray, twoDigitNum)){
            System.out.println("HOORAY!, You have won $10,000!");
            System.exit(0);
        }

        Arrays.sort(guessArray);
        Arrays.sort(twoDigitNum);

        if (Arrays.equals(guessArray, twoDigitNum)){
            System.out.println("CONGRATULATIONS!, You have won $3000!");
            System.exit(0);
        }

        if (guessArray[0] == twoDigitNum[0] ||guessArray[0] == twoDigitNum[1] ||
            guessArray[1] == twoDigitNum[0]|| guessArray[1] == twoDigitNum[1] ) {
            System.out.println("NICE!, You have won $1000!");
            System.exit(0);
            }

        for (int i = 0; i < 2; i++){
            lotteryNum *= 10;
            lotteryNum += twoDigitNum[i];
        }
        
        System.out.println("The Lottery number was " + lotteryNum + "\nTRY AGAIN NEXT TIME :)");

        s.close();
        
    }
}
