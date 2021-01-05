#include<stdio.h>

//Tower of Hanoi using recursion the time complexity is 2^n
void TOH(int n, int A, int B, int C)
{
    if (n > 0)
    {
        TOH(n - 1, A, C, B);
        printf("(%d,%d) \n", A, C);
        TOH(n - 1, B, A, C);
    }
}

int main()
{
    TOH(14, 1, 2, 3);
    return 0;
}
