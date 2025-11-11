public class AutoBoxingUnboxingDemo {
    public static void main(String[] args) {
        int a = 10;
        Integer b = Integer.valueOf(a);

        Integer c = 20;
        int d = c.intValue();

        int sum = b.intValue() + d;

        Integer result = Integer.valueOf(sum * 2);

        System.out.println("b (boxed): " + b);
        System.out.println("d (unboxed): " + d);
        System.out.println("sum (b + d): " + sum);
        System.out.println("result (sum * 2, boxed): " + result);
    }
}