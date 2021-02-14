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
    if(type == 'U')
    {
        for(; String[i] != '\0'; i++)
        {
            if(String[i] >= 'a' && String[i] <= 'z')
            {
                String[i] = String[i] - 32;
            }
        }
    }

    else
    {
        for(;String[i] != '\0'; i++)
        {
            if(String[i] >= 'A' && String[i] <= 'Z')
            {
                String[i] = String[i] + 32;
            }
        }
    }
}

//Driver Function
int main()
{
    char s[] = "GitHub";
    change_case(s,'U');
    printf("%s",s);
    return 0;
}
