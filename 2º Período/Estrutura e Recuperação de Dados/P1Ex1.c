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
    if(num <= 2) return (num == 2);
    else return primoRec(num, num - 1);
}


int main(int argc, char const *argv[])
{
    int n = 5;
    printf("\n%d",somaRec(n));
    printf("\n%d", fatRec(n));
    if(verificiacao(5)) printf("\n%d e primo.",n);
    else printf("\n%d nao e primo.", n); 
    return 0;
}
