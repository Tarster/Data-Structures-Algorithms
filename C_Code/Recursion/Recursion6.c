#include<stdio.h>

/*Program to find sum of n natural number using
1. Recursion
2. Iteration
3. Direct Formula
*/

int sumRecursion(int n)
{
    if (n < 0)
        return 0;
    else
        return sumRecursion(n - 1) + n;
}

int sumIteration(int n)
{
    int sum = 0;
    for(int i = 1; i <= n; i++)
    {
        sum += i;
    }
    return sum;
}

int sumDirect(int n)
{
    return (n * (n + 1)) / 2;
}

int main()
{
    int m = 0;
    printf("Answer using Sum Recursion function for %d is: %d \n", m, sumRecursion(m));
    printf("Answer using Sum Iteration function for %d is: %d \n", m, sumIteration(m));
    printf("Answer using Sum Direct function for %d is: %d \n", m, sumDirect(m));
    return 0;
}
