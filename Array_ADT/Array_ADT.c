#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/*
Array Abstract Data Type for representing Array with various functions
1. Creating a dynamic size array in C
2. Displaying the Array
3. Add/Append
4. Insert

Helper Functions
1. OutOfRange - For check if the length or provided index is out of bound
2. init - To initialize the array
3. Integerinput - For taking only integer inputs
*/


// Array ADT using structure
struct ARRAY_ADT
{
    int *A; // For storing the pointer to base address of the array
    int size; //For storing the size of the array
    int len; //For storing the length of the array
    int count; //For counting actual number in the array
};

/* -------------------------------HELPER FUNCTIONS----------------------------------------*/
//For taking only integer as input
int Integerinput()
{
    char *p, s[100];
    int n;
    //fgets - This function will be used to take a string input and it takes 3 parameters.
    //s - To hold the actual string that we are getting as input.
    //sizeof(s) - It is for taking the size because it will read only till sizeof(s)-1.
    //Conditions for termination of fgets - It stops when either (sizeof(s)-1) characters are read, the newline character is read, or the end-of-file is reached, whichever comes first.
    //stdin - to specify the input stream.
    while (fgets (s, sizeof(s), stdin))
    {
        //strtol - converts the initial part of the string in s to a long or int value.
        //&p - is the parameter which is used to hold the next character after the numeric value
        //Ex : 123abc in this case n will hold 123 and p will hold a location.
        //third parameter is used to provide the base as for decimal we have used 10 here we can specify any value from 2 - 36 inclusive
        n = strtol(s, &p, 10);
        if (p == s || *p != '\n')
            printf("Error!\n Please enter the integer value: ");
        else
            return n;
    }
    return -1;
}

//To check if index or length input is out of range or not.
bool OutofRange(int size, int check)
{
    if (check < 1 || check > size)
        return true;
    else
        return false;
}

// For creating and initializing the Array
struct ARRAY_ADT init()
{
    struct ARRAY_ADT Array;

    printf("Enter the size of the Array: ");
    Array.size = Integerinput();

    //Creating the pointer for the Array;
    Array.A = (int*) malloc(Array.size * sizeof(int));
    //printf("Size of from init: %d", sizeof(Array.A));
    do
    {
        printf("Enter the length of the Array: ");
        Array.len = Integerinput();
    }while(OutofRange(Array.size,Array.len));

    printf("Please enter the values in the array: ");

    for(int i = 0; i < Array.len; i++)
    {
        Array.A[i] = Integerinput();
    }

    Array.count = Array.len;

    for(int i = Array.len; i < Array.size; i++)
    {
        Array.A[i] = -1;
    }

    return Array;
}

//Function for checking the Index
bool invalidIndex(int size, int index)
{
    size--;
    if(index < 0 || index > size)
        return true;
    else
        return false;
}

/* -------------------------------OPERATIONS----------------------------------------*/

//Display Function to display the values

void display(struct ARRAY_ADT Array)
{
    for(int i = 0; i < Array.len; i++)
    {
        printf("%d \t",Array.A[i]);
    }
}

void add(struct ARRAY_ADT *Array) // I am getting the address of the structure and using it to make a call like pass by reference
{
    int lencheck = Array ->len;
    lencheck++;
    if(OutofRange(Array -> size, lencheck))
    {
        printf("Invalid Operation! Array is FULL.");
    }
    else
    {
        int num;
        printf("Enter the value to be appended: ");
        scanf("%d", &num);
        Array -> A[Array->len] = num;
        Array -> len++;
        Array -> count++;
    }
}

//Implementation of simple insert function
void insert(struct ARRAY_ADT *Array)
{
    int num;
    int index;
    int i = Array -> len - 1;
    int countcheck = Array->count;
    countcheck++;

    if(OutofRange(Array -> size, countcheck ))
    {
        printf("Invalid Operation! Array is FULL.");
        return;
    }
    else
    {
        do
        {
            printf("Enter the value to be index: ");
            scanf("%d", &index);
        }while(invalidIndex(Array->size, index));

        printf("Enter the value to be inserted: ");
        scanf("%d", &num);
        if(index >= Array->len)
        {
            Array -> A[index] = num;
            Array -> len = index + 1;
        }
        else if(index < Array->len)
        {
            Array -> A[index] = num;
        }
        else
        {
            Array -> A[index] = num;
            Array -> len++;
        }
        Array -> count++;
    }
}

/*void insert(struct ARRAY_ADT *Array)
{
    int num;
    int index;
    int i = Array -> len - 1;
    int countcheck = Array ->count;
    countcheck++;

    if(OutofRange(Array -> size, countcheck))
    {
        printf("Invalid Operation! Array is FULL.");
        return;
    }
    else
    {
        do
        {
            printf("Enter the value to be index: ");
            scanf("%d", &index);
        }while(invalidIndex(Array->size, index));

        printf("Enter the value to be inserted: ");
        scanf("%d", &num);

        if(index >= Array -> len)
        {
            Array -> A[index] = num;
            Array -> len = index+1;
        }

        else
        {
            if(Array -> A[index] == -1)
            {
                Array -> A[index] = num;
            }
            else
            {
                while(i >= index)
                {
                    Array->A[i+1] = Array->A[i];
                    i--;
                }
                Array -> A[index] = num;
                Array -> len++;
            }
        }
    }
}
*/

void deleteElement(struct ARRAY_ADT *Array)
{
    int index;
    //int i;

    do
    {
        printf("Enter the index to be deleted: ");
        scanf("%d", &index);
    }while(invalidIndex(Array -> len, index));

        /*for (i = index ;i < Array -> len; i++)
        {
            Array->A[i] = Array->A[i+1];
        }*/
        Array -> A[index] = -1;
        Array -> count--;
}



//Main Driving Function
int main()
{
    struct ARRAY_ADT Array = init();
    int choice;
    printf("*********************************************** MENU ***********************************************");
    printf("\n 1. Append");
    printf("\n 2. Insert");
    printf("\n 3. Delete");
    printf("\n 4. Display");
    printf("\n 9. Exit");

    do
    {
        printf("\n Please Enter your choice:");
        scanf("%d", &choice);
        switch(choice)
        {
            case 1: add(&Array);
                    break;
            case 2: insert(&Array);
                    break;
            case 3: deleteElement(&Array);
                    break;
            case 4: display(Array);
                    break;
            case 9: break;
            default: printf("Wrong choice please insert a valid number");

         }
    }while(choice != 9);

    return 0;
}
