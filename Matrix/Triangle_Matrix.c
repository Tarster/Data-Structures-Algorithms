#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
//Function to get input only for integer value
int get_integer()
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
    return -1;
}

//To check if user is not putting out of range values
int out_of_range_check(int size , int i ,int j)
{
    if(i < -1 || j < -1 || i >= size || j >= size)
        return true;
    else
        return false;
}


//Lower Triangle Function ROW MAJOR METHOD

//To set the value in Matrix
void set_lower_triangle_row_value(int A[], int i, int j, int value)
{ int index;
    if(i >= j)
    {
        index = ((i / 2) * (i - 1)) + j - 1;
        A[index] = value;
    }
}

//To get values from the Diagonal matrix
int get_lower_triangle_row_value(int A[], int i, int j)
{
    int index;
    //If i and j are same just send the same value at corresponding index
    if(i >= j)
    {
        index = ((i / 2) * (i - 1)) + j - 1;
        return A[index];
    }
    //Else it will be zero
    else
        return 0;
}

// Display the values
void lower_triangle_row_display(int A[], int size)
{
    for(int i = 0; i < size;i++)
    {
        for(int j = 0; j < size; j++)
        {
            printf("%d\t" ,get_lower_triangle_row_value(A, i, j));
        }
        //Change the line to print in matrix format
        printf("\n");
    }
}

//Upper Triangle Function COLUMN MAJOR METHOD

//To set the value in Matrix
void set_upper_triangle_column_value(int A[], int i, int j, int value)
{
    if(i == j)
        A[i] = value;
}

//To get values from the Diagonal matrix
int get_upper_triangle_column_value(int A[], int i, int j)
{
    //If i and j are same just send the same value at corresponding index
    if(i >= j)
        return A[i];
    //Else it will be zero
    else
        return 0;
}

// Display the values
void upper_triangle_column_display(int A[], int size)
{
    for(int i = 0; i < size;i++)
    {
        for(int j = 0; j < size; j++)
        {
            printf("%d\t" ,get_upper_triangle_column_value(A, i, j));
        }
        //Change the line to print in matrix format
        printf("\n");
    }
}

//Main Driver Method

int main()
{
    int num, choice, size = 0, i = 0, j = 0;

    //Printing the Main Menu
    printf("************************************* MAIN MENU *************************************");
    printf("\n 1. Lower Triangle Matrix.");
    printf("\n 2. Upper Triangle Matrix.");
    printf("\n 4. Exit");
    //It will Enter in the main menu
    do
    {
        printf("\n Please Enter your choice:");
        choice = get_integer();

        switch(choice)
        {
            case 1: {
                        //Write here code for Lower Triangle Matrix
                        //Taking input for the size
                        printf("Enter the size of the Diagonal Array: ");
                        num = get_integer();

                        //The actual size will be n(n-1)/2 as these are the number of non-zero elements
                        size = (num / 2) * (num + 1);

                        //Creating Diagonal Array
                        int *A = (int *) malloc(sizeof(int) * size);

                        size = num;

                        for(i = 0; i < size; i++)
                        {
                             A[i] = 0;
                        }
                        //Printing the Menu for Lower Triangle
                        printf("************************************* LOWER TRIANGLE MATRIX MENU *************************************");
                        printf("\n 1. Set value in Lower Triangle Matrix.");
                        printf("\n 2. Get value from a particular index in Lower Triangle Matrix.");
                        printf("\n 3. Display Lower Triangle Matrix.");
                        printf("\n 4.Exit");

                        do
                        {
                            printf("Please Enter your choice:");
                            choice = get_integer();

                            switch(choice)
                            {
                                case 1: {
                                            do
                                            { //Entering index values here
                                                printf("Enter the value of i: ");
                                                i = get_integer();
                                                printf("Enter the value of j: ");
                                                j = get_integer();
                                                //Checking if the values are out of range or i is not equals to j elsewhere the value is zero only
                                            }while(out_of_range_check(size, i, j) || i != j);

                                            printf("Enter the number to be place at the index[%d][%d]:", i, j);
                                            num = get_integer();
                                            //Setting the value
                                            set_lower_triangle_row_value(A, i, j, num);
                                            break;
                                        }
                                case 2: {   do
                                            {
                                                printf("Enter the value of i: ");
                                                i = get_integer();
                                                printf("Enter the value of j: ");
                                                j = get_integer();
                                            }while(out_of_range_check(size, i, j));
                                            //Just printing the value by checking out of bound
                                            printf("The value at index[%d][%d] is %d \n", i, j, get_lower_triangle_row_value(A , i, j));
                                            break;
                                        }
                                case 3: {
                                            lower_triangle_row_display(A ,size);
                                            break;
                                        }
                                case 4: return 0;
                                default: printf(" Wrong Choice! Please enter a valid option.");
                            }
                        }while(choice != 4);
                        free(A);
                        break;
                    }
            case 2: {   //Printing the Menu for Upper Triangle
                        printf("************************************* UPPER TRIANGLE MENU *************************************");
                        printf("\n 1. Set value in Upper Triangle Matrix");
                        printf("\n 2. Get value from a particular index of Upper Triangle matrix");
                        printf("\n 3. Display the Upper Triangle Matrix");
                        printf("\n 4. Exit");

                        //Taking input for the size
                        printf("Enter the size of the Diagonal Array: ");
                        num = get_integer();

                        //The actual size will be n(n-1)/2 as these are the number of non-zero elements
                        size = (num / 2) * (num + 1);

                        //Creating Diagonal Array
                        int *A = (int *) malloc(sizeof(int) * size);

                        for(; i < size; i++)
                            A[i] = 0;

                        do
                        {
                            printf("Please Enter your choice:");
                            choice = get_integer();

                            switch(choice)
                            {
                                case 1: {
                                            do
                                            { //Entering index values here
                                                printf("Enter the value of i: ");
                                                i = get_integer();
                                                printf("Enter the value of j: ");
                                                j = get_integer();
                                                //Checking if the values are out of range or i is not equals to j elsewhere the value is zero only
                                            }while(out_of_range_check(size, i, j) || i != j);

                                            printf("Enter the number to be place at the index[%d][%d]:", i, j);
                                            num = get_integer();
                                            //Setting the value
                                            set_upper_triangle_column_value(A, i, j, num);
                                            break;
                                        }
                                case 2: {   do
                                            {
                                                printf("Enter the value of i: ");
                                                i = get_integer();
                                                printf("Enter the value of j: ");
                                                j = get_integer();
                                            }while(out_of_range_check(size, i, j));
                                            //Just printing the value by checking out of bound
                                            printf("The value at index[%d][%d] is %d \n", i, j, get_upper_triangle_column_value(A , i, j));
                                            break;
                                        }
                                case 3: {
                                            upper_triangle_column_display(A ,size);
                                            break;
                                        }
                                case 4: return 0;
                                default: printf(" Wrong Choice! Please enter a valid option.");
                            }
                        }while(choice != 4);
                        free(A);
                        break;
                    }
            case 3: {
                        break;
                    }
            case 4: return 0;
            default: printf(" Wrong Choice! Please enter a valid option.");
        }
    }while(choice != 4);
    return 0;
}
