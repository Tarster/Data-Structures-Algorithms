//This file contains exercise and function related to String
#include<stdio.h>

//Function to find the length of the string
int string_length(char *string)
{
    int i = 0;
    //traversing until null-character is found
    while(string[i] != '\0')
        i++;
    //Returning i value
    return i;
}


//Driver Function
int main()
{
    char *s = "GitHub";
    printf("%d",string_length(s));
    return 0;
}
