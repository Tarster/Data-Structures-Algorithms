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
1. Out of bound check
2. Init
*/


// Array ADT using structure
struct ARRAY_ADT
{
    int *A; // For storing the pointer to base address of the array
    int size; //For storing the size of the array
    int len; //For storing the length of the array
};

/* -------------------------------HELPER FUNCTIONS----------------------------------------*/
//To check if index or length input is out of range or not.
bool OutofRange(int size, int check)
{
    if(check > size || check < 0)
        return true;
    else
        return false;
}

// For creating and initializing the Array
struct ARRAY_ADT init()
{
    struct ARRAY_ADT Array;

    printf("Enter the size of the Array: ");
    scanf("%d", &Array.size);

    do
    {
        printf("Enter the length of the Array: ");
        scanf("%d", &Array.len);
    }while(OutofRange(Array.size,Array.len));

    //Creating the pointer for the Array;
    Array.A = (int*) malloc(Array.size * sizeof(int));

    printf("Please enter the values in the arry: ");
    for(int i = 0; i < Array.len; i++)
    {
        scanf("%d", &Array.A[i]);
    }

    return Array;
}

/* -------------------------------OPERATIONS----------------------------------------*/

//Display Function to display the values
void display( struct ARRAY_ADT Array)
{
    for(int i = 0; i < Array.len; i++)
    {
        printf("%d \t",Array.A[i]);
    }
}

void add()
{
    ;
}

void insert()
{
    ;
}



//Main Driving Function
int main()
{
    struct ARRAY_ADT Array = init();
    display(Array);

    return 0;
}
