#include <iostream>
#include <math.h>  

/*int discriminant(int a, int b, int c){ 
std::cout << (b*b) - 4*a*c << std::endl; 
}*/ 

/*double a; 
double b; 
double c;*/ 

double discriminant(double a, double b, double c){ 
std::cout << (b*b) - (4*a*c) << std::endl; 
} 

double quadsolve(double a, double b, double c){ 
double discrim;
std::cout<< (b*b) - (4*a*c) <<std::endl; 
std::cin>>discrim; 

if (discrim >= 0){ 
std::cout<<((-(b) + sqrt(discrim))/(2*a))<<std::endl; 
} 
else{ 
return 0;
} 
}

int main() { 
double a = .5;
double b = 1.0;
double c = 2.0; 
std::cout << "a =" << a << std::endl; 
std::cout << "b =" << b << std::endl; 
std::cout << "c =" << c << std::endl; 
discriminant(.5,1,2); 
quadsolve(.5,1,2); 



return 0; 
} 



