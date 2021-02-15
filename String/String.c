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
    //Checking which case to return
    if(type == 'U' || type == 'u')
    {
        //Looping from 0 to null character
        for(; String[i] != '\0'; i++)
        {
            //If the character is in lower case we have to subtract 32 from the lowercase character to get the uppercase character
            if(String[i] >= 'a' && String[i] <= 'z')
            {
                String[i] -= 32;
            }
        }
    }

    // It's for getting string in lower case
    else
    {
        for(;String[i] != '\0'; i++)
        {
            //Just add the 32 to the character to change it to lowercase
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
    //traversing string from 0 to null-character
    for(int i = 0; String[i] != '\0'; i++)
    {
        //To convert the character to uppercase so we can just compare the upper case values
        temp =String[i];
        //Checking if it's actually a lowercase and than converting it
        if (temp >= 'a' && temp <= 'z')
            temp -= 32;

        //Checking if the value passed is actually a character or not
        if ((temp >= 'a' && temp <= 'z') || (temp >= 'A' && temp <= 'Z'))
        {
            //Simple checking again vowels
            if (temp == 'A' || temp == 'E' || temp == 'I' || temp == 'O' || temp == 'U')
                vowel++;
            //Else it's a consonent
            else
                consonent++;
        }
    }
    //Checking which value to return as we can only return 1 value at a time;
    if (returnArg == 'V' || returnArg == 'v')
        return vowel;
    else
        return consonent;
}

//Counting words in a string
int count_words(char *String)
{
    int i;
    int words = 1;
    //Traversing the character array
    for(i = 0; String[i] != '\0'; i++)
    {
        //Checking if the current character is space and next character is also a space or not if that happens we only want to count 1 space
        if(String[i] == ' ' && String[i+1] != ' ')
        {
            words++;
        }
    }
    //If user had used space before string termination just check for it too
    //For ex: "My string contains 5 words "
    //If the condition is not in place it will show 6 words for the string
    if(String[i-1] == ' ')
        words--;
    return words;
}

//Reversing the String
void reverse_string(char *String)
{
    //Setting j to the second last letter of the string
    int i, j = string_length(String) - 1;
    char temp = 'c';
    //Moving the loop until i is greater than j it's going to happen in mid we can use also use length - i for this trick if we know the length already
    for(i = 0; i < j; i++,j--)
    {
        //Classic swapping of the values at two indexs
        temp = String[i];
        String[i] = String[j];
        String[j] =temp;
    }
}

//Driver Function
int main()
{
    /*
    char *ss ="String_Literal";
    We can't change declared strings like this because now we hold actual address to the string literal which is a constant/read-only value.
    If we perform any operation on this it will give us memory address fault or segmentation fault.
    when we write
    char ss[] = "I can be changed";
    It creates a string literal and copy that in the array ss thus providing a character array which can be modified.
    */

    char s[] = "My string contains 5 words ";
    //vowel_consonent_count(s,'V');
    reverse_string(s);
    printf("%s",s);
    return 0;
}
