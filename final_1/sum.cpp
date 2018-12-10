#include <iostream> 

int sumofsquares(int a, int b){ 
int total;
int sum;
total = 0;
for (a;a<b+1; a = a + 1) {
sum = a * a; 
total = total + sum; 
} 
return total;

}


int main() { 
std::cout << sumofsquares(5,10) <<std::endl; 
std::cout << sumofsquares(10,12) << std::endl;
return 0;


} 



