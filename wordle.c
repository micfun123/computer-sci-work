#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// array of words for that gets loaded from a file called "words.txt"
char words[212][5];
char letters[5];
int attempts = 0;
int solved = 0;
char lastGuess[5];

char TO_LOWER(char c){
    if (c >= 'A' && c <= 'Z'){
        return c + 32;
    }
    return c;
}

void loadWords(){
    FILE *fp;
    fp = fopen("words.txt", "r");
    if (fp == NULL){
        printf("Error opening file\n");
        exit(1);
    }
    int i = 0;
    while(fscanf(fp, "%s", words[i]) != EOF){
        i++;
    }
    fclose(fp);
}

//select word
void selectWord(){
    int random = rand() % 100;
    for (size_t i = 0; i < 5; i++){
        letters[i] = words[random][i];
    }
    //make all letters lowercase
    for (size_t i = 0; i < 5; i++){
        letters[i] = TO_LOWER(letters[i]);
    }

    printf("%s\n", letters);
    printf("\n");
    //print the word

}

//main function
void main(){
    srand(time(NULL));
    loadWords();
    selectWord();
    //print the word
    printf("Welcome to Wordle!\n");
    printf("for testing purposes, the word is: %s\n", letters);
    while (attempts < 5 && solved == 0){
        printf("Guess a word: ");
        int correct = 0;
        scanf("%s", lastGuess);
        for (size_t i = 0; i < 5; i++){
            if (lastGuess[i] == letters[i]){
                printf("%c", lastGuess[i]);
                correct++;
            }
            else{
                printf("_");
            }
        }
        if (correct == 5){
            solved = 1;
            printf("\nYou win!\n");
        }
        else{
            printf("\n");
        }
        printf("\n");
        attempts++;
        
    }
}