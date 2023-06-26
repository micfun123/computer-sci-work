#include <stdio.h>

void Common_string(char *str1)
{
    char alphabet[26] = {0,0,0,0,0,0,0,0,0,0,0,0,0,
                         0,0,0,0,0,0,0,0,0,0,0,0,0};

    for (int i = 0; str1[i] != '\0'; i++)
    {
        if (str1[i] >= 'a' && str1[i] <= 'z')
        {
            alphabet[str1[i] - 'a']++;
        }
        else if (str1[i] >= 'A' && str1[i] <= 'Z')
        {
            alphabet[str1[i] - 'A']++;
        }
    }
    
    int max = 0;
    char max_char;
    for (int i = 0; i < 26; i++)
    {
        if (alphabet[i] > max)
        {
            max = alphabet[i];
            max_char = i + 'a';
        }
    }
    printf("The most common letter is %c\n", max_char);
}

int main()
{
    char str1[100];
    printf("Enter the string: ");
    scanf("%s", str1);
    Common_string(str1);
    return 0;
}

