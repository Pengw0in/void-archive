public class StringToIntegerDemo {
    public static void main(String[] args) {
        String str = "1234";

        int num1 = Integer.parseInt(str);

        Integer num2 = Integer.valueOf(str);

        System.out.println("Using parseInt: " + num1);
        System.out.println("Using valueOf: " + num2);
    }
}