public class rewrite {
    public static void main(String[] args) {

        int x = 12;
        int y = 5;
        int z;

        if (x > 10) {
            z = 3 * y;
        } else {
            z = 4 * y;
        }

        System.out.println("z: " + z);

        double c = 9000;
        double d;

        if (c > 10000) {
            d = c * 0.2;
        } else {
            d = c * 0.17 + 1000;
        }

        System.out.println("d: " + d);

        int k = 9;
        int i = 111;
        int j = 222;

        if (k % 3 == 0) {
            System.out.println(i);
        } else {
            System.out.println(j);
        }
    }
}
