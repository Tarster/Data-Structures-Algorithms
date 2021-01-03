#include<stdio.h>

//finding Factorial of n using iteration and recursion

int factorialRecursion(int n)
{
    if (n == 0)
        return 1;
    else
        return factorialRecursion(n - 1) * n;
}

int factorialIteration(int n)
{
    int fact = 1;
    for(int i = 2; i <= n; i++)
    {
        fact *= i;
    }
    return fact;
}

int main()
{
    int m = 5;
    printf("Factorial of %d using Recursion is = %d \n", m, factorialRecursion(m));
    printf("Factorial of %d using Recursion is = %d", m, factorialIteration(m));
    return 0;
}
