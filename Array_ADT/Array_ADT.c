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
//For taking only integer as input
int Integerinput()
{
    char *p, s[100];
    int n;

    while (fgets (s, sizeof(s), stdin))
    {
        n = strtol(s, &p, 10);
        if (p == s || *p != '\n')
            printf("Error!\n Please enter the integer value: ");
        else
            return n;
    }
}

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
    Array.size = Integerinput();

    //Creating the pointer for the Array;
    Array.A = (int*) malloc(Array.size * sizeof(int));

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

    return Array;
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
    ("Size: %d", Array -> size);

    if(OutofRange(Array -> size , Array -> len))
    {
        printf("Array is full");
    }
    else
    {
        int num;
        printf("Enter the value to be appended: ");
        scanf("%d", &num);
        Array -> A[Array->len] = num;
        Array -> len++;
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
    int choice;
    // add the menu here and update it regularly
    //User need to press the key
    printf("*********************************************** MENU ***********************************************");
    printf("\n 1. Append");
    printf("\n 2. Insert");
    printf("\n 3. Delete");
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
