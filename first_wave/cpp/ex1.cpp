
#include <iostream>

using namespace std;

int main(){
    cout << "Hello world! What is your name???";
    std::string name = "";
    cin >> name;
    cout << "\nHello " + name + " nice to meet you!\n";
    return 0;
}


