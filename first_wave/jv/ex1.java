// javac <name> (-o ...)
import java.util.Scanner;

class Ex1{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Hello world!\n What is your name?: ");
        String name = scan.nextLine();
        System.out.printf("Nice to meet you, %s", name);
        scan.close();
    }
}