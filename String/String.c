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

//Palindrome checking of a string
int Palindrome(char *String)
{
    //Setting j to the second last letter of the string
    int i, j = string_length(String) - 1;
    char temp = 'c';
    //Moving the loop until i is greater than j it's going to happen in mid we can use also use length - i for this trick if we know the length already
    for(i = 0; i < j; i++,j--)
    {
        //If the letters are not equal that means it's not a palindrome
        if(String[i] != String[j])
        {
            return 1;
        }
    }
    return 0;
}

//Finding Duplicate using hash table
void duplicate(char *String)
{
    int hash_Table[26] ={0};
    char temp;
    for(int i = 0; String[i] != '\0'; i++)
    {
        if ((String[i] >= 'a' && String[i] <= 'z') || (String[i] >= 'A' && String[i] <= 'Z'))
         {
             //If it's a lower case Just convert it to uppercase
             if (String[i] >= 'a' && String[i] <= 'z')
             {
                 temp = String[i] - 32;
             }
             //if already in uppercase just leave it as it is
             else
                temp = String[i];

            hash_Table[temp - 65]++;
            if(hash_Table[temp - 65] == 2)
            {
                printf("%c is occurring more than 1 time. \n", String[i]);
            }
         }
    }
}

/*
Finding duplicate in a string using bitwise operation.It will ignore the case while finding for the duplicate
Shortcoming of this is that only we can find if some element is duplicate or not. We can't find how many times it's occurring in the given string.
If an element is occurring more than 2 time for ex: 3 than it will show the duplication statement 2 times that is exactly the "time of occurrence - 1".
*/
 void duplicate_Bitwise(char *String)
 {
     int hash_bit = 0 ,mask;
     char temp;
     //Loop over the string until null-character is found
     for(int i = 0; String[i] != '\0'; i++)
     {
         //Checking if we are dealing with a character or not
         if ((String[i] >= 'a' && String[i] <= 'z') || (String[i] >= 'A' && String[i] <= 'Z'))
         {
             //If it's a lower case Just convert it to uppercase
             if (String[i] >= 'a' && String[i] <= 'z')
             {
                 temp = String[i] - 32;
             }
             //if already in uppercase just leave it as it is
             else
                temp = String[i];

            //Set the masking and merging bit to 1
            mask = 1;
            //Doing left shift bitwise operation so that 1 can be shifted to appropriate location
            mask = mask << temp - 65;

            //Checking using masking(AND) if the bit at that place is 1 or 0,if it evaluate to 1 we print the duplicate vaiable
            if(mask & hash_bit)
            {
                printf("%c is occurring more than 1 time. \n", temp);
            }
            //Just set the appropriate bit to 1 using the merging(OR) operation
            else
                hash_bit = hash_bit | mask;
        }
     }
 }

 //Function to find the anagram
 int Anagram(char *String1, char *String2)
 {
     int hash_table[26] = {0};
     int i = 0;
     char temp;
     if(string_length(String1) == string_length(String2))
     {
         return 1;
     }
     for(;String1[i] != '\0';i++)
     {
         if ((String1[i] >= 'a' && String1[i] <= 'z') || (String1[i] >= 'A' && String1[i] <= 'Z'))
         {
             //If it's a lower case Just convert it to uppercase
             if (String1[i] >= 'a' && String1[i] <= 'z')
             {
                 temp = String1[i] - 32;
             }
             //if already in uppercase just leave it as it is
             else
                temp = String1[i];

             hash_table[temp - 65]++;
         }
     }
     for(i = 0; String2[i] != '\0'; i++)
     {
         if ((String2[i] >= 'a' && String2[i] <= 'z') || (String2[i] >= 'A' && String2[i] <= 'Z'))
         {
             //If it's a lower case Just convert it to uppercase
             if (String2[i] >= 'a' && String2[i] <= 'z')
             {
                 temp = String2[i] - 32;
             }
             //if already in uppercase just leave it as it is
             else
                temp = String2[i];

             hash_table[temp - 65]--;
             if(hash_table[temp - 65] < 0)
                return 1;
         }
     }

    return 0;
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

    char s[] = "Observer";
    char s1[] = "varbose";
    //vowel_consonent_count(s,'V');
    //reverse_string(s);
   // Anagram(s,s1);
    printf("%d", Anagram(s,s1));
    return 0;
}
