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
    if(check < -1 || check > size)
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

    printf("Please enter the values in the array: ");
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

void add(struct ARRAY_ADT *Array) // I am getting the address of the struct and using it to make a call like pass by reference
{
    int num;
    printf("Enter the value to be appended: ");
    scanf("%d", &num);

    if(OutofRange(Array -> size,Array -> len))
    {
        printf("Array is full:");
    }
    else
    {
        Array->A[Array->len] = num;
        Array->len++;
    }
}

void insert(struct ARRAY_ADT *Array)
{
    int num;
    int index;
    int i = Array -> len - 1;

    printf("Enter the value to be inserted: ");
    scanf("%d", &num);

    printf("Enter the value to be index: ");
    scanf("%d", &index);

    if(OutofRange(Array -> size, Array -> len))
    {
        printf("Array is full:");
    }
    else
    {
        if (OutofRange(Array -> size, index))
        {
            printf("Index is not valid");
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

void deleteElement(struct ARRAY_ADT *Array)
{
    int index;
    int i = Array -> len - 1;

    printf("Enter the index to be deleted: ");
    scanf("%d", &index);

    if (OutofRange(Array -> len, index))
    {
        printf("Index is not valid");
    }
    else
    {
        for (i = index ;i < Array -> len; i++)
        {
            Array->A[i] = Array->A[i+1];
        }

        Array -> len--;
        Array -> A[Array -> len] = 0;
    }
}



//Main Driving Function
int main()
{
    struct ARRAY_ADT Array = init();
    //insert(&Array);
    deleteElement(&Array);
    display(Array);
    return 0;
}
