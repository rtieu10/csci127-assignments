#include <iostream>
#include <math.h>  

int discriminant(int a, int b, int c){ 
return (b*b)-(4*a*c); 
} 

double quadsolve(double a, double b, double c){ 
int d; 
d = discriminant(a,b,c);

if (d >= 0){ 
return (-b+ sqrt(d))/(2*a)); 
} 
else{ 
return 0;
} 
}

int main() { 
std::cout << discriminant(3,1,2) << std::endl; 
std::cout << quadsolve(3,1,2) << std::endl; 

return 0; 
} 



