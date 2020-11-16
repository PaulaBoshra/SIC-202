#include <stdio.h>
#include <stdlib.h>

void main()
{
    int i, num[2];
    
    FILE *pointer;
    pointer = fopen("task4.txt", "a+");
    
    for (i = 0; i < 2; i++)
    {
        fscanf(pointer, "%d", &num[i]);
    }
    fprintf(pointer, "\nSum = %d",num[0] + num[1]);
    printf("\nDone");
    fclose(pointer );
}