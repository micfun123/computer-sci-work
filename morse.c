
#include <stdio.h>
#include <stdint.h>

int main(){

    char messageout[100];
    char messagein[100];
    char Morse[26][5] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",
                         ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                         "...","-","..-","...-",".--","-..-","-.--","--.."};
    printf("What is your message: ");
    scanf("%s",messageout);

    for (int i = 0; i < 100; i++)
    {
        if (messageout[i] == '\0')
        {
            break;
        }
        else
        {
            int j = messageout[i] - 97;
            printf("%s ",Morse[j]);
            
        }
    }



}