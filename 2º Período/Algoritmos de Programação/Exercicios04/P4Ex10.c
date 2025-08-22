#include <stdio.h>

int main()
{
    int vetor[10] = {1,2,3,4,5,6}, aux;
    for(int i = 0; i < 6; i++)
    {
        if(i > 2)
        {
            vetor[i + 1] = vetor[i];
            aux = vetor[i + 1]
        }
        

    }
    vetor[3] = 9;
    for(int i =0; i < 7; i++)
    {
        printf("%d\n",vetor[i]);
    }
}