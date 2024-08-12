#include<stdio.h>

//This program demonstrates indirect recursion

void functionTwo(int n);

//This is first function that is calling the another function
void functionOne(int n)
{
    if (n > 0)
    {
        printf("%d", n);
        functionTwo(n-1);
    }
}

//Than this calls function one again creating a recursion stack
void functionTwo(int n)
{
    if (n > 1)
    {
        printf("%d", n);
        functionOne(n/2);
    }
}

int main()
{
    functionOne(20);
    return 0;
}
