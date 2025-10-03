#include <stdio.h>
#include <stdbool.h>

int somaRec(int num)
{
    if(num == 1) return 1;
    else return (num + somaRec(num - 1));
}

int fatRec(int num)
{
    if(num == 1) return 1;
    else return (num * fatRec(num - 1));
}

bool primoRec(int num, int div)
{
    if(div == 1) return true;
    if(num % div == 0) return false;
    else return primoRec(num, div - 1);
}

bool verificiacao(int num)
{
    if(num < 2) return (num == 2);
    else return primoRec(num, num - 1);
}
void encontrarPrimosRec(int num, int* vet, int* cont)
{
    if(num < 2) return;
    encontrarPrimosRec(num-1,vet,cont);
    if (primoRec(num, num - 1))
    {
        vet[*cont] = num;
        (*cont)++;
    }
}

void ordCrescenteRec(int* vet, int* cont)
{
    
}

int main(int argc, char const *argv[])
{
    int n = 15,contador = 0;
    int vetor[100];
    printf("\n%d",somaRec(n));
    printf("\n%d", fatRec(n));
    if(verificiacao(5)) printf("\n%d e primo.\n",n);
    else printf("\n%d nao e primo.\n", n); 
    encontrarPrimosRec(n,vetor,&contador);
    for(int i = 0; i < contador; i++)
    {
        printf("%d\t",vetor[i]);
    }
    return 0;
}
