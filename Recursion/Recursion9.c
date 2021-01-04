#include<stdio.h>

//Normal Taylor Series Implementation using recursion and Iteration
double taylorSeriesRecursion(int x, int n)
{
    static double p = 1, f = 1;
    double r;
    if(n == 0)
        return 1.0;
    else
    {
        r =taylorSeriesRecursion(x, n - 1);
        p *= x;
        f *= n;
        return r + p / f;
    }
}

double taylorSeriesIteration(int x, int n)
{   int i;
    double s = 1.0;
    double p = 1.0;
    double f = 1.0;

    for(i = 1; i < n; i++)
    {
        p *= x;
        f *= i;
        s = s + (p / f);
    }
    return s;
}

//Taylor Series using Hornet Formula

double taylorSeriesHornetRecursion(int x, int n)
{
    static double s = 1;
    if (n == 0)
    {
        return s;
    }
    else
    {
        s = 1 + (x * s) / n;
        return taylorSeriesHornetRecursion(x, n - 1);
    }
}

double taylorSeriesHornetIteration(int x, int n)
{
    double series = 1;
    for(;n > 0; n--)
    {
       series = 1 + (x  * series) / n;
    }
    return series;
}

int main()
{
    printf("%f \n", taylorSeriesRecursion(2,1000));
    printf("%f \n", taylorSeriesIteration(2,1000));
    printf("%f \n", taylorSeriesHornetIteration(2,1000));
    printf("%f", taylorSeriesHornetRecursion(2,1000));
    return 0;
}
