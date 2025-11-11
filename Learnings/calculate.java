public class calculate {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle();

        rect.height = 10.3;
        rect.width = 32.1;

        System.out.println(rect.volume);
        System.out.println(rect.perimeter);

    }
}

class Rectangle {
    double height;
    double width;

    double volume = width * height;
    double perimeter = 2*(width + height);
}
