#include<stdio.h>

//Created a fun that shows recursion and this function first print than call the recursive function
void loadingfun(int n)
{
    if(n>0)
    {
        printf("%d \t",n);
        loadingfun(n-1);
    }
}

//This function print the output at the time of return rather than at the start.
void returningfun(int n)
{
    if(n>0)
    {
        returningfun(n-1);
        printf("%d \t",n);
    }
}

//Main for calling both the functions
int main()
{
    int x =4;
    printf("Loading Function \n");
    loadingfun(x);
    printf("\nReturning Recursive Function \n");
    returningfun(x);
    return 0;
}
