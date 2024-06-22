/*
I made it with Jahir Acevedo. UNI's student
*/

#include <iostream>

int main()
{
    int combination = 1;
    int total = 0;
    for (int i = 0; i <=2; i++){
        for (int j = 0; j <=4; j++){
            for (int k = 0; k <=10; k++){
                for (int l = 0; l <=20; l++){
                    for (int m = 0; m <=40; m++){
                        for (int n = 0; n <=100; n++){
                            for (int o = 0; o <=200; o++){
                                total = (100*i) + (50*j) + (20*k) + (10*l)+ (5*m) + (2*n) + (1*o);
                                if (total == 200){
                                    combination++;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    std::cout << combination << std::endl;
    return 0;
}
