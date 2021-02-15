//This file contains exercise and function related to String
#include<stdio.h>

//Function to find the length of the string
int string_length(char *String)
{
    int i = 0;
    //traversing until null-character is found
    while(String[i] != '\0')
        i++;
    //Returning i value
    return i;
}

//Uppercase or Lowercase
void change_case(char *String, char type)
{
    int i = 0;
    if(type == 'U' || type == 'u')
    {
        for(; String[i] != '\0'; i++)
        {
            if(String[i] >= 'a' && String[i] <= 'z')
            {
                String[i] -= 32;
            }
        }
    }

    else
    {
        for(;String[i] != '\0'; i++)
        {
            if(String[i] >= 'A' && String[i] <= 'Z')
            {
                String[i] += 32;
            }
        }
    }
}

//counting consonents and vowels
int vowel_consonent_count(char *String, char returnArg)
{
    char temp ='c';
    int consonent = 0;
    int vowel = 0;
    for(int i = 0; String[i] != '\0'; i++)
    {
        temp =String[i];
        if (temp >= 'a' && temp <= 'z')
            temp -= 32;

        if ((temp >= 'a' && temp <= 'z') || (temp >= 'A' && temp <= 'Z'))
        {
            if (temp == 'A' || temp == 'E' || temp == 'I' || temp == 'O' || temp == 'U')
                vowel++;
            else
                consonent++;
        }
    }
    if (returnArg == 'V' || returnArg == 'v')
        return vowel;
    else
        return consonent;
}


//Driver Function
int main()
{
    char s[] = "GitHub";
    //vowel_consonent_count(s,'V');
    printf("%d",vowel_consonent_count(s,'c'));
    return 0;
}
