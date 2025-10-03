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

int func6(const char *str)
{
    int tamanho = 0;
    while(str[tamanho] != '\0')
    {
        tamanho++;
    }
    return tamanho;
}

int func7(const char *str, char ch)
{
    int tamanho = 0,contador = 0; 
    while(str[tamanho] != '\0')
    {
        if(str[tamanho] == ch) contador++;
        tamanho++;
    }
    return contador;
}

void func8(const char *str, char *copia)
{
    int tamanho = 0;
    while(str[tamanho] != '\0')
    {
        copia[tamanho] = str[tamanho];
        tamanho++;
    }
    copia[tamanho] = '\0';
}

bool func9(const char *str)
{
    char stringReversa[100];
    int j = 0;
    for(int i = func6(str) - 1;i >= 0; i--)
    {
        stringReversa[j] = str[i];
        j++;
    }
    stringReversa[j] = '\0';
    if (strcmp(str,stringReversa) == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void func10(char *str)
{
    int tamanho = 0;
    while(str[tamanho] != '\0')
    {
        str[tamanho] = toupper(str[tamanho]);
        tamanho++;
    }
}

void PrintVector(int sz,int vec[sz])
{
    printf("%d\n",vec[sz]);
}

void Swap(int *a, int *b)
{
    int aux = *a;
    *a = *b;
    *b = aux;
}

void OrdenarCrescente(int sz, int vec[sz])
{
    bool mustStop = false;
    while (mustStop == false)
    {
        mustStop = true;
        for(int i = 0; i < sz;i++)
        {
            if(vec[i] > vec[i+1])
            {
                Swap(&vec[i],&vec[i+1]);
                mustStop = false;
            }
        }
    }
}

void SeparaParImpar(int sz,int vec[sz],int vPar[],int vImpar[], int *szPar, int *szImpar)
{
    for(int i = 0; i < sz;i++)
    {
        if(vec[i] % 2 == 0)
        {
            vPar[*szPar] = vec[i];
            szPar++;
        }
        else
        {
            vImpar[*szImpar] = vec[i];
            szImpar++;
        }
    }
}

int main(int argc, char const *argv[])
{
    int n = 5;
    int n2 = 21;
    const char *stringOriginal = "Ola Mundo.";
    char stringCopiada[100];
    int vet[10] = {10,9,8,7,6,5,4,3,2,1};
    int vetP[100], vetI[100];
    int *a = 0, *b = 0;
    bool ehPar = func1(n);
    printf("%d\n",ehPar);
    double nReal = func2();
    double fReal = func3(nReal);
    printf("%lf\n",fReal);
    int fatN = func4(n);
    printf("%d\n", fatN);
    printf("%d\n",func5(n, n2));
    printf("%d\n",func6(stringOriginal)); 
    printf("%d\n",func7("arara", 'a')); 
    func8(stringOriginal, stringCopiada);
    printf("Copia: %s\n",stringCopiada);
    printf("%d\n",func9(stringOriginal));
    func10(stringCopiada);
    printf("%s\n",stringCopiada);
    for(int i = 0; i < 10; i++)
    {
        PrintVector(i,vet);
    }
    Swap(&n,&n2);
    printf("%d %d\n",n,n2);
    OrdenarCrescente(10,vet);
    for(int i = 0; i < 10; i++)
    {
        PrintVector(i,vet);
    }    
    SeparaParImpar(10, vet,vetP,vetI,a,b);
    for(int i = 0;i < *a;i++)
    {
        printf("%d ",vetP[i]);
    }
    return 0;
}
