#include<stdio.h>

//This program shows the tree recursion use debug to run it step by step
// to understand it.
void TreeRecursion(int n)
{
    if(n>0)
    {
        printf("%d ",n);
        TreeRecursion(n-1);
        TreeRecursion(n-1);
    }
}
int main()
{
    int m =3;
    TreeRecursion(m);
    return 0;
}
