#include<stdio.h>

void negLeftposRight(int array[],int n)
{
    int i = 0;
    int j = n - 1;
    int temp = 0;
    while(i < j)
    {
        while(array[i] < 0)
            i++;
        while(array[j] >= 0)
            j--;
        if(i < j)
        {
            temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }
}


int main()
{
    int array[10];
    int size;
    printf("Enter the size of the Array: ");
    scanf("%d",&size);

    printf("Please enter the numbers in the array: ");
    for(int i = 0; i < size; i++)
        scanf("%d", &array[i]);

    negLeftposRight(array,size);
    for(int i = 0; i < size; i++)
        printf("%d \t", array[i]);

    return 0;
}
