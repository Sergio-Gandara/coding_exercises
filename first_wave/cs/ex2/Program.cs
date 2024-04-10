

using System;

namespace MyBoxBuilder{

    public class Box{
        
        char verticalWall='|';
        char horizontalWall='-';
        char boxSpace=' ';
        int[] resolution={0, 0};
        // string[resolution[0]][resolution[1]] entityList;
        string rules;
        public Box(int xSize=20, int ySize=20, string rule="none"){
            this.resolution[0] = xSize;
            this.resolution[1]=ySize; 
            this.rules=rules;   
        }

            
        public void Draw(){
            for(int j=0; j<=resolution[1]; j++){
                if(j==0 || j==resolution[0]){
                    for(int k=0; k<=resolution[0]; k++){
                        Console.Write(horizontalWall);
                    }
                    Console.Write('\n');
                    continue;
                }
                for(int i=0; i<=resolution[0]; i++){
                    if(i==0 || i==resolution[1]){
                        Console.Write(verticalWall);
                        continue;
                    }
                    EntityDrawer(i, j);
                    //Console.Write(boxSpace); // free space to modify
                }
                Console.Write('\n');
            }
        }

        public void EntityDrawer(int xPosition, int yPosition){
            if(!(String.Equals(this.rules, "even2*"))){
                if((xPosition+yPosition)%2==0){
                    Console.Write('*');
                    return;
                }
                Console.Write(" ");
                return;
            }
        }

        


    }
    public class MainClass{
        public static void Main(){
            System.Console.WriteLine("Welcome to the box constructer!");
            int[] data={0, 0};
            try{
                System.Console.WriteLine("Please write X and Y size for resolution: ");
                data[0] = int.Parse(System.Console.ReadLine());
                data[1] = int.Parse(System.Console.ReadLine());
                Box myBox = new Box(data[0], data[1]);
                myBox.Draw();
            }
            catch (Exception e){
                System.Console.WriteLine(e.ToString());
            }
        }
    }
}