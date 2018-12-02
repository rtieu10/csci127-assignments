#include <iostream> 



/* make user pick a number between 0 and 99, use a while loop to guess the number and go up and down until it gets the right number for each uess the computer will print the guess and ask if it's lower, higher, or correct the user will input an int response using -1 to represent if the num is lower than the guess 1 to show the number is higher and 0 if the number is correct */ 

int main() {
    int a;
    int guess;
    int response; 

    guess = rand() % 100; //set guess to a random number between 0 - 99

    std::cout << "Enter a number between 0 - 99";
    std::cin >> a;
    std::cout << "Guess: " << guess << std::endl; 
    std::cout << "If the guess is higher enter 1, if the number is lower enter -1, if the guess  			  is correct enter 0" << std::endl; 
    std::cin >> response; 

    while (response != 0) {   // if the number is not correct 
	if (response == 1) { 
             guess = rand() % guess + 0;
	}                                   //if the guess is greater than pick a random number 						between 0 and the guess for a lower number 
       	else { 
               guess = rand() % 100 + guess  // if the number is less than then pick a great num
        }
        
      std::cout << "New guess: " << guess << std::endl; 
      std::cout << "If the guess is higher enter 1, if the number is lower enter -1, if the guess  			  is correct enter 0" << std::endl; 
      std::cin >> response;
return 0 
} 

/* keeps giving an error regarding the use of rand() says it was not 'declared' not sure why */ 


