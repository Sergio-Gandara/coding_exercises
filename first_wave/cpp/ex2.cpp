
#include <iostream>
#include <array>
#include <string>
using namespace std;


static std::array<int,2>resolution={};
std::array<int,2> ask_size(){
    std::array<int,2> resolution={}; // working with these types of arrays return better results.
    cout << "Please introduce the X size of the box: ";
    cin >> resolution[0];
    cout << "Now introduce the Y size: ";
    cin >> resolution[1];
    return resolution;
}

int update_space(int mode=0, std::string mode_args="foo", std::array<int,2> position={0}){
    /* This function prints the appropiate value for each space in the matrix.
       This function has 2 modes:
        SETUP MODE: (mode=0)
        Entities and apparition rules are set. Map size is set.
        PRINT MODE: (mode=1)
        Uses saved data to proceed (we do this by use of static variables)
    */
    static std::string rules;
    char map_space=' ';
    switch(mode){
    case 0:
        resolution =  ask_size(); // if working with ordinary arrays, this would not work.
        rules = mode_args;
        //
        break;
    case 1:
        if(rules.compare("even2*")){
            if(((position[0] + position[1]) % 2) == 0){
                cout << '*';
            }
            else{
                cout << map_space;
            }
            
            //cout << position[0] + position[1];
        }
        
        //
        break;
    default:
        cout << "Unkwon mode";
        return -1;
   }
   return 0;
}

void map_builder(){
    char map_limit_vertical='_';
    char map_limit_horizontal='|';
    char map_space=' ';
    std::string mode = "even2*";
        
    int height=0;
    for(int i=0; i<=resolution[1]; i++){ // this section of the code prints a box
        if(i==0 || i==resolution[1]){
            for (int j=0; j<=resolution[0]; j++){
                cout << map_limit_vertical;
            }
        }
        else{
            for (int j=0;j<=resolution[0]; j++){
                if(j==0 || j==resolution[0]){
                cout <<  map_limit_horizontal;
                continue;
            }
            std::array <int,2> position={i, height};
            update_space(1, mode, position);
            height++;
            //cout << map_space; // or print whatever we need
        }
    }
    
    cout << '\n';
    }
}


int main(int argc, char **argv) 
{
    cout << "Welcome to the box printer!";
    std::string mode = "foo";
    update_space(0, mode);
    
    map_builder();



    
    return 0;
}
