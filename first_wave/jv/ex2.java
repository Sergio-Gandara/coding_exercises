
import java.util.Scanner;
public class ex2 {
    public static void main(String[] args){
        int xSize;
        int ySize;
        System.out.println("Welcome to the Box drawer!");
        Scanner scan = new Scanner(System.in);
        System.out.println("Please introduce resolution values for X and Y values: ");
        xSize=Integer.valueOf(scan.nextLine());
        ySize=Integer.valueOf(scan.nextLine());
        scan.close();
        
        Box myBox = new Box(xSize, ySize);
        myBox.Draw();

    }
}
