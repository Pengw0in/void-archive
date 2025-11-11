import java.util.Scanner;

class BankAccount {
    String depositorName;
    int accountNumber;
    String accountType;
    double balance;
    
    BankAccount(String name, int accNum, String accType, double initialBalance) {
        depositorName = name;
        accountNumber = accNum;
        accountType = accType;
        balance = initialBalance;
    }
    
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: $" + amount + ", New balance: $" + balance);
        } else {
            System.out.println("Invalid amount!");
        }
    }
    
    public void withdraw(double amount) {
        if (amount > 0 && balance >= amount) {
            balance -= amount;
            System.out.println("Withdrawn: $" + amount + ", New balance: $" + balance);
        } else {
            System.out.println("Invalid amount or insufficient balance: $" + balance);
        }
    }
    
    public void display() {
        System.out.println("Account Holder: " + depositorName + ", Balance: $" + balance);
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter name: ");
        String name = input.nextLine();
        System.out.print("Enter account number: ");
        int accNum = input.nextInt();
        input.nextLine();
        System.out.print("Enter account type: ");
        String accType = input.nextLine();
        System.out.print("Enter initial balance: ");
        double initialBalance = input.nextDouble();

        BankAccount account = new BankAccount(name, accNum, accType, initialBalance);
        account.display();
        
        System.out.print("\nDeposit amount: ");
        account.deposit(input.nextDouble());
        
        System.out.print("Withdraw amount: ");
        account.withdraw(input.nextDouble());
        
        input.close();
    }
}