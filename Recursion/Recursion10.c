#include<stdio.h>
#define MAX 50
//Program to find nth element in Fibonacci series using different methods
//Because of memorization we now can only calculate 50 term at max using memorization for calculating above
//that we need to increase the MAX

int F[MAX];

int fibonacciIteration(int n)
{
    int first = 0, second = 1, ending = 1;
    if (n <= 1 )
        return n;
    else
    {
        for(int i = 2; i <= n; i++)
        {
            ending = first + second ;
            first = second;
            second = ending;
        }
        return ending;
    }
}

int fibonacciRecursion(int n)
{
    if(n <= 1)
        return n;
    else
        return fibonacciRecursion(n - 1) + fibonacciRecursion(n - 2);
}

int fibonacciRecursionMemorization(int n)
{
    if(n <= 1)
        return n;
    else
    {
        if(F[n - 2] == -1)
            F[n - 2] = fibonacciRecursionMemorization(n - 2);
        if(F[n - 1] == -1)
            F[n - 1] = fibonacciRecursionMemorization(n - 1);

        return  F[n - 2] + F[n - 1];
    }
}

void initializerGlobalArray_F(int f[])
{
    for(int i =0; i < MAX; i++)
    {
        f[i] = -1;
    }
}

int main()
{
    int m = 7;
    initializerGlobalArray_F(F);
    printf("The %d term of the Fibonacci series using the Iteration is: %d \n", m, fibonacciIteration(m));
    printf("The %d term of the Fibonacci series using the Recursion is: %d \n", m, fibonacciRecursion(m));
    printf("The %d term of the Fibonacci series using the Recursion with Memorization is: %d", m, fibonacciRecursionMemorization(m));
    return 0;
}
