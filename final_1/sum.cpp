#include <iostream> 

int sumofsquares(int a, int b){ 
int total = 0; 
int sum; 

for (a; b; a++) { 
std::cout<<a*a<<std::endl; 
std::cin>>sum; 
total = total + sum; 
return total; 
} 

}


int main() { 
sumofsquares(5,10); 
sumofsquares(10,12);



} 



