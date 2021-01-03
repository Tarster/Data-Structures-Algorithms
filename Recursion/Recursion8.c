#include<stdio.h>

/* Writing pow function of c using 3 different methods
1. Recursion
2. Modified Recursion
3. Iteration
*/

long powerRecursion(int m, int n)
{
    if (n == 0)
        return 1;
    else
        return powerRecursion(m, n - 1) * m;
}

long powerRecursionModified(int m, int n)
{
    if (n == 0)
        return 1;
    if(n % 2 == 0)
        return powerRecursionModified(m * m, n / 2);
    else
        return m * powerRecursionModified(m * m, (n - 1) / 2);
}

long powerIteration(int m, int n)
{
    long power = 1;
    for(int i = 0; i < n; i++)
    {
        power *= m;
    }
    return power;
}

int main()
{
    int m = 2;
    int n = 10;

    printf("The power of %d to %d using Recursion function is: %d \n", m, n, powerRecursion(m, n));
    printf("The power of %d to %d using Modified Recursion function is: %d \n", m, n, powerRecursionModified(m, n));
    printf("The power of %d to %d using Recursion function is: %d \n", m, n, powerIteration(m, n));
    return 0;
}
