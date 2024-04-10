
public class Box{
    char verticalWall='|';
    char horizontalWall='-';
    char boxSpace=' ';
    private String rules="even2*";
    int[] resolution={10, 10};

    public Box(int xSize, int ySize){
        resolution[0]=xSize;
        resolution[1]=ySize;
    }

    public void EntityDrawer(int xPosition, int yPosition){
        if(((this.rules.equals("even2*")))){
            if((xPosition+yPosition)%2==0){
                System.out.print('*');
                return;
            }
            
        }
        System.out.print(" ");
        return;
    }

    public void Draw(){
        for(int j=0; j<=resolution[1]; j++){
            if(j==0 || j==resolution[0]){
                for(int k=0; k<=resolution[0]; k++){
                    System.out.print(horizontalWall);
                }
                System.out.print('\n');
                continue;
            }
            for(int i=0; i<=resolution[0]; i++){
                if(i==0 || i==resolution[1]){
                    System.out.print(verticalWall);
                    continue;
                }
                EntityDrawer(i, j);
                //System.out.print(boxSpace); // free space to modify
            }
            System.out.print('\n');
    }
}
}