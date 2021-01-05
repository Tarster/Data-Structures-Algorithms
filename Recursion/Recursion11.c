#include<stdio.h>

// Find Combination nCr using recursion(Pascal Triangle Algorithm)

int CombinationRecursion(int n, int r)
{
    if(r == 0 || r == n)
        return 1;
    else
        return CombinationRecursion(n - 1, r - 1) + CombinationRecursion(n - 1, r);
}

int main()
{
    int m = 4, n = 4;
    printf("The value of %dC%d is: %d", m, n, CombinationRecursion(m, n));
    return 0;
}
