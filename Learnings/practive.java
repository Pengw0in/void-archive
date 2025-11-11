import java.util.Scanner;
// import java.util.Random;
// import java.util.Arrays;
import java.io.*;

class volume{
    int h;
    int w;
    static int x;

    volume(){
        h = 10;
        w = 20;
    }

    volume(int h, int w){
        this.h = h;
        this.w = w;
    }

    void cal() {
        System.out.println(h*w);
    }

    static void cal(int h, int w){
        System.out.println(h*w);
    }
}

public class practive {
    public static void main(String[] args) throws IOException{

        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);

        String line = br.readLine();           // Read a line
        int character = br.read();             // Read a character
        // Random r = new Random();
        // Integer x = r.nextInt(10) + 10;
        // System.out.println(x);

        // int[] guess = new int[2];
        // int[] letsee = new int[] {1,2,3,4};

        Scanner s = new Scanner(System.in);

        s.nextInt(10);
        

        volume v = new volume();
        v.cal();
        volume.cal(7,8);
        System.out.println(volume.x);
    }
}