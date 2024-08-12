#include<stdio.h>

//Program to demonstrate static variable in Recursion

int StaticRecursion(int n)
{
    static int x = 0;

    if(n>0)
    {
        x++;
        return StaticRecursion(n-1) + x;
    }

    return 0;
}


//Main for calling the functions
int main()
{
    int m = 6;
    printf("%d",StaticRecursion(m));
    return 0;
}

