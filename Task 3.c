#include <stdio.h>
#include <stdlib.h>

int i, j,x,count, num, sum, total, arr[20];

int sum_of_elements (int *arr) 
{
for (i = 0; i < 20; i++)
sum += arr[i];
return sum;
}

void main()
{
    printf("Enter the values:\n");
        for (i = 0; i < 20; i++)
        {
            count = 1;
            scanf("%d",&num);
                for (j = 0; j < i; j++)
                {
                    if (arr[j] == num)
                    {
                        count = 0;
                    }
                }
                    if (count == 1)
                    {
                        arr[x] = num;
                        x++;
                    }
        }
printf("The unique values are: ");
for (i = 0; i < x; i++)
    {
        printf("%d",arr[i]);
    }
    total = sum_of_elements(arr);
    printf("\nThe sum of unique values = %d",total);
}
