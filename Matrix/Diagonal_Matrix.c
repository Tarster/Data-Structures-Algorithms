#include <stdio.h>

int get_integer()
{
    char *p, s[100];
    int n;
    while ((getchar()) != ‘\n’);
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


int out_of_range_check(int size , int i ,int j)
{
    if(i < -1 || j < -1 || i >= size || j >= size)
        return 0;
    else
        return 1;
}

void set_value(int A[], int i, int j, int value)
{
    if(i == j)
        A[i - 1] = value;
}

int get_value(int A[], int i, int j)
{
    if(i == j)
        return A[i - 1];
    else
        return 0;
}

void display(int A[], int size)
{
    for(int i = 0; i < size;i++)
        for(int j = 0; j < size; j++)
            printf()
}

int main()
{
    int size;

    //Taking input for the size
    printf("Enter the size of the Diagonal Array");
    size = ;

    //Creating Diagonal Array
    int *A = (int) malloc(sizeof(int));


    return 0;
}
