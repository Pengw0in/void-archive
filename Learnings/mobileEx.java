public class mobileEx {
    public static void main(String[] args) {
        Mobile m1 = new Mobile();

        m1.company = "Mototrola";
        m1.model = "Edge 50 Neo";
        m1.version = 15.6;
        m1.color = "Pantone Red";

        System.out.println("MObile Information");
        System.out.println("Company: " + m1.company);
        System.out.println("Model: " + m1.model);
        System.out.println("Version: " + m1.version);
        System.out.println("color: " + m1.color);
    }
}

class Mobile {
    String company;
    String model;
    double version;
    String color;
}
