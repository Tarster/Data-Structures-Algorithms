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

// I am getting the address of the structure and using it to make a call like pass by reference
void add(struct ARRAY_ADT *Array)
{
    int lencheck = Array ->len;
    lencheck++;
    //Getting length and increasing it by 1 so that it can be checked for Full Array
    if(OutofRange(Array -> size, lencheck))
    {
        printf("Invalid Operation! Array is FULL.");
    }
    // Array is not full resume our operations;
    else
    {
        //getting the actual number now
        int num;
        printf("Enter the value to be appended: ");
        scanf("%d", &num);
        //Setting the number to the place and incrementing length by 1
        Array -> A[Array->len] = num;
        Array -> len++;
        // We have added 1 number so count should also be increamented
        Array -> count++;
    }
}

//Implementation of simple insert function
// The Idea was to shift elements to add elements in between which is quite possible but then we can add only in between.
// So to  circumvent that I made function like this
void insert(struct ARRAY_ADT *Array)
{
    int num;
    int index;
    int countcheck = Array->count;
    countcheck++;
    // Number can't be added as Array is full rightnow
    if(OutofRange(Array -> size, countcheck ))
    {
        printf("Invalid Operation! Array is FULL.");
        return;
    }
    // Array is not full still there is some space
    else
    {
        do
        {
            printf("Enter the value to be index: ");
            scanf("%d", &index);
        }while(invalidIndex(Array->size, index));

        printf("Enter the value to be inserted: ");
        scanf("%d", &num);

        /* We have to insert element at a place when length is less than index;
           For ex: Size : 4  Length: 1
           we choose an index 3 which is valid now length should be set to 4
           as we can access index 0-3 now.
        */
        if(index >= Array->len)
        {
            Array -> A[index] = num;
            Array -> len = index + 1;
        }

        //In this case chosen index is less than the length so either we are updating
        //or inserting a value at the position which contains a initial value of -1;
        else
        {
            // If it's -1 we want to update the count variable as well
            if(Array -> A[index] == -1)
                Array -> A[index] = num;
            // If we are updating just set the number and return
            else
            {
                Array -> A[index] = num;
                return ;
            }
        }
        // Update the count as a new number is added right now
        Array -> count++;
    }
}
//Deleting the Element
void deleteElement(struct ARRAY_ADT *Array)
{
    int index;

    do
    {
        printf("Enter the index to be deleted: ");
        scanf("%d", &index);
    }while(invalidIndex(Array -> len, index));

    // If the number is -1 at the required index than we can just return
    if(Array -> A[index] == -1)
        return;
    // We need to empty the number and set it to -1 and decrement the value of count by 1
    else
    {
        Array -> A[index] = -1;
        Array -> count--;
    }
}

// Linear search with shifting implemented to shift searched element one block before so that in the next search 1 iteration less should be taken by the system
int linearSearchWithShifting(struct ARRAY_ADT array)
{
    int num = 0;
    printf("Please enter the number to be searched: ");
    num =Integerinput();
    for(int i = 0; i < array.len; i++)
    {
        if(array.A[i] == num)
        {
            if(i != 0)
            {
                int temp;
                temp = array.A[i-1];
                array.A[i-1] = array.A[i];
                array.A[i] = temp;
                return i-1;
            }
            return i;
        }
    }
return -1;
}
//Daily Commit
//Binary Search using loop
int binarySearch(struct ARRAY_ADT Array )
{
    printf("Please enter the number to be searched: ");
    int num =Integerinput();
    // Storing lower and upper number
    int lower = 0;
    int upper = Array.len;

    //Will not exit unit lower is high so number is not found
    while (lower <= upper)
    {
        int middle = (lower + upper) / 2;
        //Comparing the number
        if(Array.A[middle] == num)
            return middle;
        //If number is less than this going to happen or else will execute
        else if(Array.A[middle] < num)
            lower = middle + 1;
        else
            upper = middle - 1;
    }
    //Number not found return -1
    return -1;
}

// Return element at a certain index
int getElement(struct ARRAY_ADT array)
{
    int index;
    do
    {
        printf("Please enter the index: ");
        index = Integerinput();
    }while(invalidIndex(array.size,index));
    return array.A[index];
}

void setElement(struct ARRAY_ADT *array)
{
    int index, num;
    do
    {
        printf("Please enter the index: ");
        index = Integerinput();
    }while(invalidIndex(array->size,index));

    printf("Please enter the numerical value: ");
    num =Integerinput();

    array -> A[index] = num;
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
    printf("\n 5. Linear Search");
    printf("\n 6. Binary Search");
    printf("\n 7. Get Element");
    printf("\n 8. Set Element");
    printf("\n 9. Exit");

    do
    {
        printf("\nPlease Enter your choice:");
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
            case 5: {
                        int num = linearSearchWithShifting(Array);
                        if(num == -1)
                            printf("Number does not exist in the list");
                        else
                            printf("Number is located at %d position.", num);
                        break;
                    }
            case 6:{
                        int num = binarySearch(Array);
                        if(num == -1)
                            printf("Number does not exist in the list");
                        else
                            printf("Number is located at %d position.", num);
                        break;
                   }
            case 7: {
                        int num = getElement(Array);
                        printf("The number at the desired index is: %d", num );
                        break;
                    }
            case 8: setElement(&Array);
                    break;
            case 9: break;
            default: printf("Wrong choice please insert a valid number");

         }
    }while(choice != 9);

    return 0;
}
