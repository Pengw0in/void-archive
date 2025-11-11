import java.util.Scanner;

public class Book {
    int code;
    String title;
    double price;
    
    public Book() {
        code = 0;
        title = "Unknown";
        price = 0.0;
    }
    
    public Book(int bookCode, String bookTitle, double bookPrice) {
        this.code = bookCode;
        this.title = bookTitle;
        this.price = bookPrice;
    }
    
    public void displayBook() {
        System.out.println("Book Code: " + code);
        System.out.println("Book Title: " + title);
        System.out.println("Book Price: $" + price);
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter book code: ");
        int code = input.nextInt();
        input.nextLine();
        System.out.print("Enter book title: ");
        String title = input.nextLine();
        System.out.print("Enter book price: ");
        double price = input.nextDouble();
        
        Book book = new Book(code, title, price);
        book.displayBook();
        
        input.close();
    }
}
