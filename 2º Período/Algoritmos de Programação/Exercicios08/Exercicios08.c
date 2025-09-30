#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool func1(int num)
{
    bool _ehPar = true;
    if (num % 2 != 0)
    {
        _ehPar = false;
    }
    return _ehPar;
}

double func2()
{
    double _num = 0;
    printf("Entre com um numero real: ");
    scanf("%lf",&_num);
    return _num;
}

double func3(double num)
{
    int _numInteiro = (int) num;
    return ((double) num - (int) _numInteiro);
}

int func4(int num)
{
    int _somaFat = 1;
    for(int i = num;i > 0; i--)
    {
        _somaFat *= i;
    }
    return _somaFat;
}

int func5(int a, int b)
{
    if (a < b)
    {
        for(int i = a; i < b;i++)
        {
            if(i % 2 == 0)
            {
                printf("%d\t",i);
            }
        }
    }
    else
    {
        for(int i = b; i < a; i++)
        {
            if(i % 2 == 0)
            {
                printf("%d\t",i);
            }
        }
    }
}

char func6(const char *str)
{
    int tamanho = 0;
    while(str[tamanho] != '\0')
    {
        tamanho++;
    }
    return tamanho;
}

char func7(const char *str, char ch)
{
    int tamanho = 0; 
    while(str[tamanho] != '\0')
    {
        
        tamanho++;
    }
}

int main(int argc, char const *argv[])
{
    int n = 5;
    int n2 = 21;
    bool ehPar = func1(n);
    printf("%d\n",ehPar);
    double nReal = func2();
    double fReal = func3(nReal);
    printf("%lf\n",fReal);
    int fatN = func4(n);
    printf("%d\n", fatN);
    printf("%d\n",func5(n, n2));
    printf("%d\n",func6("Ola Mundo."));
    return 0;
}
