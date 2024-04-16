#include <iostream>
#include <vector>


// Customed datatype
typedef std::string text_t;
// beter 
using text_d = std::string;

namespace first{
    int x = 1;
}

namespace second{
    int y = 2;
}

int main(){

    int age = 33;

    const double my_age = 33.000;

    double proce = 500.200;

    char myName = 'T';
 
    std::string myName2 = "Tim";

    bool myBoool = false;

    text_t my_text = "myName?";

    text_t my_textN = "myName!!!Iwantgo why";

    std::cout << "what are you doing?" << std::endl;
    std::cin >> age;

    std::cout << age << std::endl;
    std::cout << first::x << std::endl;
    std::cout << second::y;

    return 0;

}