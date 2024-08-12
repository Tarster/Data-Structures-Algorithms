#include<stdio.h>

//This creates a nested recursion and every time the output will be 91 if input is less than 100
int nestedRecursion(int n)
{
    if (n > 100)
        return n - 10;
    return nestedRecursion(nestedRecursion(n + 11));
}

int main()
{
    printf("%d \n", nestedRecursion(50));
    return 0;
}
